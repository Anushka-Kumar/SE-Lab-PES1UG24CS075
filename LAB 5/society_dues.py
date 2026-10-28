"""Manage apartment society maintenance dues."""

import ast
import operator
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)


def add_due(flat, month, amount, history=None):
    """Add a maintenance due and record it in the history."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues VALUES (?, ?, ?, 0)",
        (flat, month, amount),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Collect payment and return the amount if the due exists."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
            (flat, month),
        )
        return row[0]

    return None


def _evaluate_arithmetic(node):
    """Evaluate a restricted arithmetic expression safely."""
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
    }

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in operations:
        left = _evaluate_arithmetic(node.left)
        right = _evaluate_arithmetic(node.right)
        return operations[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and isinstance(
        node.op, (ast.UAdd, ast.USub)
    ):
        operand = _evaluate_arithmetic(node.operand)
        return operand if isinstance(node.op, ast.UAdd) else -operand

    raise ValueError("Unsupported arithmetic expression")


def penalty(rule):
    """Calculate a late fee from a safe arithmetic expression."""
    try:
        expression = ast.parse(rule, mode="eval")
        return _evaluate_arithmetic(expression.body)
    except (
        ValueError,
        SyntaxError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
    ):
        return 0


def pending():
    """Return the flats with unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()
    return [row[0] for row in rows]


def main():
    """Demonstrate the society dues ledger."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()

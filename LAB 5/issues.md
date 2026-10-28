# Lab 5: Static Code Analysis

## 1. Issue Table

| No. | Tool | Issue Identified | Solution Implemented |
|:---:|---|---|---|
| 1 | Pylint | Missing module and function docstrings | Added descriptive docstrings to the module and functions. |
| 2 | Pylint | Function name did not follow the snake_case naming convention | Renamed `addDue()` to `add_due()`. |
| 3 | Pylint | Mutable default argument used in a function | Replaced `history=[]` with `history=None` and initialized the list inside the function. |
| 4 | Pylint | Inconsistent return statements | Added an explicit `return None` when no matching maintenance due exists. |
| 5 | Pylint | Incorrect comparison with `None` and code-quality issues | Corrected the comparison logic and improved code readability. |
| 6 | Bandit | Hardcoded password in the source code | Removed the unused hardcoded password constant. |
| 7 | Bandit | Potential SQL injection vulnerability | Replaced the SQL f-string with a parameterized query using placeholders. |
| 8 | Bandit | Unsafe use of `eval()` | Replaced `eval()` with a restricted arithmetic expression evaluator using Python's `ast` module. |
| 9 | Flake8 | Lines exceeding the maximum permitted length | Split long statements across multiple lines. |
| 10 | Flake8 | Incorrect blank-line spacing and formatting | Corrected blank-line spacing and formatted the code according to PEP 8 conventions. |

## 2. Final Static Analysis Results

| Tool | Final Result | Status |
|---|---|:---:|
| Pylint | Score: 10.00/10 | PASS |
| Bandit | No issues identified | PASS |
| Flake8 | No errors reported | PASS |

## 3. Conclusion

The program was analyzed using Pylint, Bandit, and Flake8. The identified code-quality, security, and formatting issues were addressed. The final version achieved a Pylint score of 10.00/10, with no issues reported by Bandit and no errors reported by Flake8.
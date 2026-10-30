### 1. What is static code analysis, and why is it important?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, code-quality problems, and formatting issues early in development. This improves code reliability, readability, security, and maintainability.

### 2. What issues did you identify using Pylint, Bandit, and Flake8?

Pylint identified code-quality issues such as missing docstrings, naming convention violations, mutable default arguments, and inconsistent return statements. Bandit identified security concerns involving a hardcoded password, potentially unsafe SQL string formatting, and the use of `eval()`. Flake8 identified formatting problems, including long lines and incorrect blank-line spacing.

### 3. How did you fix the identified issues?

I added docstrings, followed snake_case naming conventions, replaced the mutable default argument with `None`, and corrected return statements. I replaced unsafe SQL string formatting with parameterized queries, removed the hardcoded password, and replaced `eval()` with a restricted arithmetic expression evaluator. I also corrected line lengths and formatting issues.

### 4. What challenges did you face while fixing the issues?

One challenge was fixing security issues without changing the program's expected behavior. Replacing `eval()` required implementing a safer way to evaluate arithmetic expressions. I also had to rerun the static analysis tools to verify that the reported issues were resolved and that the updated code met the required quality and formatting standards.

### 5. What did you learn from this lab?

I learned that static analysis tools can identify issues that may not be apparent when a program runs successfully. Pylint helps improve code quality, Bandit identifies potential security vulnerabilities, and Flake8 checks coding style and formatting. Using these tools together helps produce cleaner, safer, and more maintainable Python code.

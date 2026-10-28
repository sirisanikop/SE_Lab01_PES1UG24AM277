# Static Analysis Issues

Use the original reports (`pylint_before.txt`, `bandit_before.txt`, and
`flake8_before.txt`) as the evidence for the initial findings.

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Shell command built by string concatenation | Security (Bandit B605, High) | 71 | `os.system()` executes a command through a shell and the `server` value is concatenated into the command, creating possible command injection. | Use `subprocess.run()` with a list of arguments and `check=True`, avoiding shell interpretation. |
| Insecure temporary filename | Security (Bandit B306, Medium) | 66 | `tempfile.mktemp()` chooses a filename without securely creating the file. | Use `NamedTemporaryFile()` to create a unique temporary file and return its path. |
| Hard-coded password constant | Security (Bandit B105, Low) | 6 | A password-like value is stored directly in source code; it is unused in this demo. | Remove the unused hard-coded password constant. |
| Pseudo-random generator for coin toss | Security (Bandit B311, Low) | 61 | `random.choice()` is not intended for security-sensitive randomness. | Use `secrets.choice()` for a secure choice. |
| Mutable default argument | Code quality (Pylint W0102) | 11 | `players=[]` reuses the same list object across calls when no players are provided. | Use `None` as the default and create a new list inside the function. |
| Non-snake_case names and missing docstrings | Code quality (Pylint) | Multiple | Several functions and arguments do not follow Python naming conventions and functions lack docstrings. | Rename functions/arguments to snake_case and add docstrings. |
| Whitespace/style issues | Style (Flake8) | 5, 60, 79, 87 | Spacing around a dictionary colon, blank lines, missing whitespace after a comma, and inline-comment spacing violate style rules. | Apply PEP 8 formatting. |

## Verification results

After replacing the source with the corrected version, run the tools locally and
record their actual output. Do not claim a score or a clean report until you have
run the tools on your machine.

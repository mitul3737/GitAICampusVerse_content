# GitHub Copilot Instructions for PEP8 Python Coding

## Purpose
This document provides instructions for GitHub Copilot to follow PEP8 standards when generating Python code. These guidelines ensure the code is clean, readable, and adheres to widely accepted Python best practices.

## General Guidelines
1. Follow the [PEP8](https://peps.python.org/pep-0008/) style guide strictly.
2. Ensure all generated code uses 4 spaces per indentation level.
3. Line length should not exceed 79 characters.
4. Include proper documentation for all classes, methods, and functions (docstrings).
5. Avoid trailing whitespace at the end of lines.

## Naming Conventions
- Use `snake_case` for variables, functions, and method names.
- Use `PascalCase` for class names.
- Constants should be in `ALL_CAPS`.

## Import Statements
- Always place import statements at the top of the file.
- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application or library-specific imports
- Use one import per line.

## Best Practices
1. Always use explicit relative imports.
2. Avoid wildcard imports (e.g., `from module import *`).
3. Prefer f-strings over other string formatting methods.
4. Handle exceptions explicitly and avoid bare `except` clauses.

## Example
```python
# Correct way to write a function adhering to PEP8 standards

def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of the two numbers.
    """
    return a + b
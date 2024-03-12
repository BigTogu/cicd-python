# CICD for Python Project

This repository is configured with GitHub Actions to automatically run the tests whenever there's a new push or pull request on the repository. The workflow configuration file (.github/workflows/tests.yml) defines the steps to set up the Python environment, install dependencies, and execute the tests using unittest This ensures that the tests are executed in a continuous integration (CI) environment, providing immediate feedback on the code changes.

# Running Tests in Python

This repository contains Python files for basic mathematical operations (`suma.py`, `resta.py`, `multiplicacion.py`, `division.py`) along with their respective test files (`test_suma.py`, `test_resta.py`, `test_multiplicacion.py`, `test_division.py`).

## Running Tests with unittest

To run the tests using `unittest`:

1. Make sure you have Python installed on your system.
2. Navigate to the directory containing the Python files and the test files.
3. Create a Python script (e.g., `run_tests.py`) and include the following code:

```python
import unittest
from tests.test_suma import TestSumar
from tests.test_resta import TestRestar
from tests.test_multiplicacion import TestMultiplicar
from tests.test_division import TestDividir


if __name__ == '__main__':
    unittest.main()
```

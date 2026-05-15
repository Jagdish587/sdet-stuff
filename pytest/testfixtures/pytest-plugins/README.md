# Pytest Plugins and Shared Fixtures Example

This project demonstrates how to organize reusable fixtures in `pytest` using:

* `pytest_plugins`
* shared fixture modules
* modular fixture structure
* root-level `conftest.py`
* API/UI test separation

It also explains the modern recommended structure after the deprecation of defining `pytest_plugins` inside nested `conftest.py` files.

---

# Project Structure

```text
project/
│
├── conftest.py
├── pytest.ini
│
└── tests/
    │
    ├── __init__.py
    │
    ├── fixtures/
    │   ├── __init__.py
    │   ├── api.py
    │   ├── auth.py
    │   ├── db.py
    │   └── users.py
    │
    ├── api/
    │   └── test_api.py
    │
    └── ui/
        └── test_ui.py
```

---

# Purpose

This repository demonstrates:

* How to share fixtures across unrelated test folders
* How fixture dependency injection works in pytest
* How to organize scalable test infrastructure
* How to avoid deprecated `pytest_plugins` usage in nested `conftest.py`

---

# Requirements

* Python 3.10+
* pytest 8+

---

# Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Install pytest:

```bash
pip install pytest
```

---

# Root `conftest.py`

The root-level `conftest.py` registers reusable fixture modules globally.

```python
pytest_plugins = [
    "tests.fixtures.api",
    "tests.fixtures.auth",
    "tests.fixtures.db",
    "tests.fixtures.users",
]
```

Why root-level?

Newer pytest versions no longer allow:

```python
pytest_plugins = [...]
```

inside nested `conftest.py` files.

This now causes:

```text
Defining 'pytest_plugins' in a non-top-level conftest is no longer supported
```

because plugins affect the entire pytest session globally.

---

# `pytest.ini`

```ini
[pytest]

addopts = -ra -q

pythonpath = .

testpaths =
    tests

python_files = test_*.py

markers =
    api
    ui
    db
    slow
```

## Explanation

### `addopts = -ra -q`

* `-q`

  * quiet output

* `-ra`

  * show summary for skipped/errors/failures

### `pythonpath = .`

Adds project root to Python import path.

### `testpaths`

Tells pytest where tests are located.

### `markers`

Registers custom markers.

---

# Fixture Modules

## `tests/fixtures/db.py`

Contains database-related fixtures.

Example:

```python
import pytest


@pytest.fixture(scope="session")
def db_connection():
    return {
        "host": "localhost",
        "database": "test_db",
    }
```

---

## `tests/fixtures/auth.py`

Contains authentication fixtures.

Example:

```python
import pytest


@pytest.fixture
def auth_token():
    return "jwt-token"
```

---

## `tests/fixtures/api.py`

Contains API client fixtures.

Example:

```python
import pytest


@pytest.fixture
def api_client(auth_token):
    return {
        "token": auth_token,
    }
```

Notice:

`api_client` depends on `auth_token`.

Pytest resolves dependencies automatically.

---

# Running Tests

Run all tests:

```bash
pytest
```

Run only API tests:

```bash
pytest tests/api/
```

Run only UI tests:

```bash
pytest tests/ui/
```

Run tests by marker:

```bash
pytest -m api
```

Skip slow tests:

```bash
pytest -m "not slow"
```

---

# Example Output

```text
.......

7 passed in 0.15s
```

---

# Key Concepts

## 1. Fixtures

Fixtures provide reusable setup and teardown logic.

Example:

```python
@pytest.fixture
def sample_user():
    return {"name": "Alice"}
```

---

## 2. Fixture Injection

Pytest injects fixtures automatically by function argument name.

```python
def test_user(sample_user):
    assert sample_user["name"] == "Alice"
```

---

## 3. Fixture Dependencies

Fixtures can depend on other fixtures.

```python
@pytest.fixture
def api_client(auth_token):
    ...
```

Pytest builds the dependency graph automatically.

---

## 4. Shared Fixtures

Shared fixtures should live in reusable modules instead of huge monolithic `conftest.py` files.

Recommended:

```text
tests/fixtures/
```

---

# Best Practices

## Recommended

* Keep fixtures modular
* Use root-level `conftest.py` for plugin registration
* Use markers for grouping tests
* Keep API/UI fixtures separated
* Use fixture dependency injection instead of manual setup

## Avoid

* Giant `conftest.py` files
* Duplicate setup logic
* Nested `pytest_plugins`
* Direct imports from `conftest.py`

---

# References

* pytest official docs
* pytest fixtures documentation
* pytest plugin system documentation

---

# License

MIT License

# project/conftest.py

pytest_plugins = [
    "tests.fixtures.api",
    "tests.fixtures.auth",
    "tests.fixtures.db",
    "tests.fixtures.users",
]
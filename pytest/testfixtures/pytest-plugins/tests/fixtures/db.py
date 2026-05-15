# tests/fixtures/db.py

import pytest


@pytest.fixture(scope="session")
def db_connection():
    print("\nConnecting to test database")

    db = {
        "host": "localhost",
        "port": 5432,
        "database": "test_db",
    }

    yield db

    print("\nClosing database connection")
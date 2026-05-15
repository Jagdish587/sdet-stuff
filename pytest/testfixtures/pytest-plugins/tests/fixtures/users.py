# tests/fixtures/users.py

import pytest


@pytest.fixture
def sample_user():
    return {
        "id": 101,
        "name": "Alice",
        "role": "admin",
    }


@pytest.fixture
def normal_user():
    return {
        "id": 102,
        "name": "Bob",
        "role": "user",
    }
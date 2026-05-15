# tests/fixtures/auth.py

import pytest


@pytest.fixture
def auth_token():
    return "jwt-token-123"


@pytest.fixture
def auth_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }
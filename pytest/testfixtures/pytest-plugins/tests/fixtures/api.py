# tests/fixtures/api.py

import pytest


@pytest.fixture
def api_base_url():
    return "https://api.example.com"


@pytest.fixture
def api_client(api_base_url, auth_headers):
    return {
        "base_url": api_base_url,
        "headers": auth_headers,
    }
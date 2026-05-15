# tests/api/test_api.py

import pytest


@pytest.mark.api
def test_api_base_url(api_client):
    assert api_client["base_url"] == "https://api.example.com"


@pytest.mark.api
def test_auth_header_exists(api_client):
    assert "Authorization" in api_client["headers"]


@pytest.mark.api
@pytest.mark.db
def test_database_name(db_connection):
    assert db_connection["database"] == "test_db"


@pytest.mark.api
def test_sample_user_role(sample_user):
    assert sample_user["role"] == "admin"


@pytest.mark.slow
def test_slow_processing():
    result = sum(range(1000))
    assert result > 0
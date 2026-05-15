import pytest
import requests


BASE_URL = "https://dummy-api.com"


@pytest.fixture(scope="session")
def auth_token():

    login_payload = {
        "username": "admin",
        "password": "password123"
    }

    print("\nLogging into application...")

    response = requests.post(
        f"{BASE_URL}/login",
        json=login_payload
    )

    assert response.status_code == 200

    response_data = response.json()

    token = response_data["token"]

    print(f"\nJWT Token: {token}")

    return token


@pytest.fixture
def auth_headers(auth_token):

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    return headers
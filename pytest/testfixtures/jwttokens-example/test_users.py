import requests


BASE_URL = "https://dummy-api.com"


def test_get_users(auth_headers):

    response = requests.get(
        f"{BASE_URL}/users",
        headers=auth_headers
    )

    print(response.json())

    assert response.status_code == 200
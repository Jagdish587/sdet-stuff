import requests


BASE_URL = "https://dummy-api.com"


def test_create_order(auth_headers):

    order_payload = {
        "product_name": "iPhone",
        "quantity": 2
    }

    response = requests.post(
        f"{BASE_URL}/orders",
        json=order_payload,
        headers=auth_headers
    )

    print(response.json())

    assert response.status_code == 201
import requests


BASE_URL = "http://127.0.0.1:8000"


# 1. Login using Basic Authentication
response = requests.post(
    f"{BASE_URL}/login",
    auth=("alice", "password123")
)

if response.status_code != 200:
    print("Login failed")
    print(response.text)
    exit()

token = response.json()["access_token"]

print("Login successful")
print("Token:", token)


# 2. Use JWT to get notes
response = requests.get(
    f"{BASE_URL}/notes",
    headers={
        "Authorization": f"Bearer {token}"
    }
)

if response.status_code == 200:
    print("Notes:")
    print(response.json())
else:
    print("Failed to get notes")
    print(response.text)

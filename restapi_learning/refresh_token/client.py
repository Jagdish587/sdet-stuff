import requests
import time

BASE = "http://localhost:8000"

print("---- LOGIN ----")
r = requests.post(f"{BASE}/login")
tokens = r.json()

access_token = tokens["access_token"]
refresh_token = tokens["refresh_token"]

print("Access token:", access_token)
print("Refresh token:", refresh_token)

headers = {
    "Authorization": f"Bearer {access_token}"
}

print("\n---- PROTECTED (initial) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.json())

print("\nWaiting for access token to expire...")
time.sleep(12)

print("\n---- PROTECTED (expired access token) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.status_code, r.text)

print("\n---- REFRESH ACCESS TOKEN ----")
r = requests.post(f"{BASE}/refresh", params={"refresh_token": refresh_token})
new_access = r.json()["access_token"]

print("New access token:", new_access)

headers["Authorization"] = f"Bearer {new_access}"

print("\n---- PROTECTED (after refresh) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.json())


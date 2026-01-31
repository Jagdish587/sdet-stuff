import requests
import time

BASE = "http://localhost:8000"

print("---- LOGIN ----")
r = requests.post(f"{BASE}/login")
refresh_token = r.json()["refresh_token"]
print("Refresh token:", refresh_token)

print("\n---- GET ACCESS TOKEN ----")
r = requests.post(f"{BASE}/token", params={"refresh_token": refresh_token})
access_token = r.json()["access_token"]
print("Access token:", access_token)

headers = {
    "Authorization": f"Bearer {access_token}"
}

print("\n---- PROTECTED ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.json())

print("\nWaiting for access token to expire...")
time.sleep(5)

print("\n---- PROTECTED (expired) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.status_code, r.text)


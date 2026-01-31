import requests
import time

BASE = "http://localhost:8000"

print("---- LOGIN ----")
r = requests.post(f"{BASE}/login")
data = r.json()

access_token = data["access_token"]
print("Access token:", access_token)
print("Expires in:", data["expires_in"], "seconds")

headers = {
    "Authorization": f"Bearer {access_token}"
}

print("\n---- PROTECTED (immediate) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.json())

print("\nSleeping until token expires...")
time.sleep(12)

print("\n---- PROTECTED (after expiry) ----")
r = requests.get(f"{BASE}/protected", headers=headers)
print(r.status_code, r.text)


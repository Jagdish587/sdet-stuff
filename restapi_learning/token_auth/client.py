import requests

BASE = "http://localhost:8000"

print("---- PUBLIC ----")
r = requests.get(f"{BASE}/public")
print(r.json())

print("\n---- PROTECTED (no token) ----")
r = requests.get(f"{BASE}/protected")
print(r.status_code, r.text)

print("\n---- PROTECTED (wrong token) ----")
r = requests.get(
    f"{BASE}/protected",
    headers={"Authorization": "Bearer wrongtoken"}
)
print(r.status_code, r.text)

print("\n---- PROTECTED (valid token) ----")
r = requests.get(
    f"{BASE}/protected",
    headers={"Authorization": "Bearer secrettoken123"}
)
print(r.json())


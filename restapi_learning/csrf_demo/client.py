import requests

client = requests.Session()

print("---- LOGIN ----")
r = client.get("http://localhost:8000/login")
data = r.json()
print("data = ", data)
csrf_token = data["csrf_token"]

print("Response:", data)
print("Stored cookies:", client.cookies)

print("\n---- TRANSFER WITHOUT CSRF ----")
r = client.post("http://localhost:8000/transfer")
print(r.text)

print("\n---- TRANSFER WITH CSRF ----")
r = client.post(
    "http://localhost:8000/transfer",
    headers={"X-CSRF-Token": csrf_token}
)
print(r.json())


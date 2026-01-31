import requests

client = requests.Session()

print("---- LOGIN ----")
r = client.get("http://localhost:8000/login")
print("Response:", r.json())
print("Stored cookies:", client.cookies)

print("\n---- PROFILE ----")
r = client.get("http://localhost:8000/profile")
print("Response:", r.json())
print("new Stored cookies:", client.cookies)


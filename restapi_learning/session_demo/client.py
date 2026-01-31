import requests

client = requests.Session()

print("---- CALL /profile BEFORE login ----")
r = client.get("http://localhost:8000/profile")
print(r.json())

print("\n---- LOGIN ----")
r = client.get("http://localhost:8000/login")
print(r.json())
print("Stored cookies:", client.cookies)

print("\n---- CALL /profile AFTER login ----")
r = client.get("http://localhost:8000/profile")
print(r.json())


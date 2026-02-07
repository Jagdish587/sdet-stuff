import requests
import time

URL = "http://127.0.0.1:8000/api"

for i in range(6):
    r = requests.get(URL)
    print(f"Request {i+1}: {r.status_code}, {r.json()}")
    time.sleep(1)


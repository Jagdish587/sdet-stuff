import requests
import time

URL = "http://127.0.0.1:8000/api"

for i in range(6):
    start = time.time()
    r = requests.get(URL)
    elapsed = time.time() - start

    print(f"Request {i+1}: status={r.status_code}, time={elapsed:.2f}s")


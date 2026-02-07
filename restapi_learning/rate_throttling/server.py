from fastapi import FastAPI, Request
import time
from collections import defaultdict, deque

app = FastAPI()

MAX_REQUESTS = 3
TIME_WINDOW = 10
THROTTLE_DELAY = 2

clients = defaultdict(deque)

@app.get("/api")
async def api(request: Request):
    client_ip = request.client.host
    now = time.time()
    q = clients[client_ip]

    while q and now - q[0] > TIME_WINDOW:
        q.popleft()

    if len(q) >= MAX_REQUESTS:
        time.sleep(THROTTLE_DELAY)

    q.append(now)

    return {"message": "Request processed"}


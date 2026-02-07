from fastapi import FastAPI, Request, HTTPException
import time
from collections import defaultdict, deque

app = FastAPI()

MAX_REQUESTS = 3
TIME_WINDOW = 10  # seconds

clients = defaultdict(deque)

@app.get("/api")
async def api(request: Request):
    client_ip = request.client.host
    now = time.time()
    q = clients[client_ip]

    # Remove expired timestamps
    while q and now - q[0] > TIME_WINDOW:
        q.popleft()

    # Rate limit check
    if len(q) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    q.append(now)
    return {"message": "Request successful"}


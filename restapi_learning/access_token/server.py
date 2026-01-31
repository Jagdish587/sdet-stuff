from fastapi import FastAPI, Header, HTTPException
import uuid
import time

app = FastAPI()

# token -> { user, expires_at }
ACCESS_TOKENS = {}

ACCESS_TOKEN_TTL = 10  # seconds (short on purpose for demo)

@app.post("/login")
def login():
    token = str(uuid.uuid4())
    expires_at = time.time() + ACCESS_TOKEN_TTL

    ACCESS_TOKENS[token] = {
        "user": "alice",
        "expires_at": expires_at
    }

    return {
        "access_token": token,
        "token_type": "Bearer",
        "expires_in": ACCESS_TOKEN_TTL
    }


@app.get("/protected")
def protected(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Missing Authorization header")

    try:
        scheme, token = authorization.split()
    except ValueError:
        raise HTTPException(400, "Invalid Authorization format")

    if scheme.lower() != "bearer":
        raise HTTPException(400, "Unsupported auth scheme")

    token_data = ACCESS_TOKENS.get(token)
    if not token_data:
        raise HTTPException(401, "Invalid token")

    if time.time() > token_data["expires_at"]:
        raise HTTPException(401, "Access token expired")

    return {"message": f"hello {token_data['user']}"}


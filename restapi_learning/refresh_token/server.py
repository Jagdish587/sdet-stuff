from fastapi import FastAPI, Header, HTTPException
import uuid
import time

app = FastAPI()

ACCESS_TTL = 10      # seconds (short for demo)
REFRESH_TTL = 60     # seconds

# token stores
ACCESS_TOKENS = {}    # access_token -> {user, expires_at}
REFRESH_TOKENS = {}   # refresh_token -> {user, expires_at}

@app.post("/login")
def login():
    user = "alice"

    access_token = str(uuid.uuid4())
    refresh_token = str(uuid.uuid4())

    ACCESS_TOKENS[access_token] = {
        "user": user,
        "expires_at": time.time() + ACCESS_TTL
    }

    REFRESH_TOKENS[refresh_token] = {
        "user": user,
        "expires_at": time.time() + REFRESH_TTL
    }

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
        "access_expires_in": ACCESS_TTL,
        "refresh_expires_in": REFRESH_TTL
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
        raise HTTPException(401, "Invalid access token")

    if time.time() > token_data["expires_at"]:
        raise HTTPException(401, "Access token expired")

    return {"message": f"hello {token_data['user']}"}


@app.post("/refresh")
def refresh(refresh_token: str):
    token_data = REFRESH_TOKENS.get(refresh_token)
    if not token_data:
        raise HTTPException(401, "Invalid refresh token")

    if time.time() > token_data["expires_at"]:
        raise HTTPException(401, "Refresh token expired")

    new_access_token = str(uuid.uuid4())
    ACCESS_TOKENS[new_access_token] = {
        "user": token_data["user"],
        "expires_at": time.time() + ACCESS_TTL
    }

    return {
        "access_token": new_access_token,
        "expires_in": ACCESS_TTL
    }


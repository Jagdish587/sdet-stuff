from fastapi import FastAPI, Header, HTTPException
from jose import jwt, JWTError
import time
import uuid

app = FastAPI()

# ======================
# CONFIG (PRACTICE MODE)
# ======================
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

ACCESS_TTL = 2* 60      # 2 minute
REFRESH_TTL = 5 * 60 # 5 minutes

# refresh_token -> { user, expires_at }
REFRESH_TOKENS = {}

def create_access_token(user: str):
    now = int(time.time())
    payload = {
        "sub": user,
        "iat": now,
        "exp": now + ACCESS_TTL
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login")
def login():
    user = "alice"

    refresh_token = str(uuid.uuid4())
    REFRESH_TOKENS[refresh_token] = {
        "user": user,
        "expires_at": time.time() + REFRESH_TTL
    }

    return {
        "refresh_token": refresh_token,
        "refresh_expires_in_seconds": REFRESH_TTL,
        "access_expires_in_seconds": ACCESS_TTL
    }

@app.post("/token")
def token(refresh_token: str):
    token_data = REFRESH_TOKENS.get(refresh_token)
    if not token_data:
        raise HTTPException(401, "Invalid refresh token")

    if time.time() > token_data["expires_at"]:
        raise HTTPException(401, "Refresh token expired")

    access_token = create_access_token(token_data["user"])

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in_seconds": ACCESS_TTL
    }

@app.get("/protected")
def protected(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Missing Authorization header")

    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(401, "Invalid auth scheme")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload["sub"]

    except JWTError:
        raise HTTPException(401, "Invalid or expired access token")

    return {
        "message": f"hello {user}",
        "access_token_valid_for_seconds": payload["exp"] - int(time.time())
    }


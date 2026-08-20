from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import secrets
from datetime import datetime, timedelta, timezone

app = FastAPI()

basic_auth = HTTPBasic()
bearer_auth = HTTPBearer()

SECRET_KEY = "my-secret-key"


# Existing users
users = {
    "alice": {
        "password": "password123",
        "user_id": 1
    },
    "bob": {
        "password": "password456",
        "user_id": 2
    }
}


notes = [
    {
        "id": 1,
        "user_id": 1,
        "title": "Alice Note",
        "content": "Hello Alice"
    },
    {
        "id": 2,
        "user_id": 2,
        "title": "Bob Note",
        "content": "Hello Bob"
    }
]


# -------------------------
# LOGIN
# -------------------------

@app.post("/login")
def login(
    credentials: HTTPBasicCredentials = Depends(basic_auth)
):
    user = users.get(credentials.username)

    if not user or not secrets.compare_digest(
        credentials.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    payload = {
        "user_id": user["user_id"],
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# -------------------------
# AUTHENTICATION
# -------------------------

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_auth)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload["user_id"]

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# -------------------------
# GET NOTES
# -------------------------

@app.get("/notes")
def get_notes(
    user_id: int = Depends(get_current_user)
):
    return [
        note["content"]
        for note in notes
        if note["user_id"] == user_id
    ]

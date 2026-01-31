from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Pretend database
TOKENS_DB = {
    "secrettoken123": "alice",
    "admintoken456": "admin"
}

@app.get("/public")
def public():
    return {"message": "anyone can see this"}

@app.get("/protected")
def protected(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, "Missing Authorization header")

    # Expect: Authorization: Bearer <token>
    try:
        scheme, token = authorization.split()
    except ValueError:
        raise HTTPException(400, "Invalid Authorization format")

    if scheme.lower() != "bearer":
        raise HTTPException(400, "Unsupported auth scheme")

    user = TOKENS_DB.get(token)
    if not user:
        raise HTTPException(401, "Invalid token")

    return {"message": f"hello {user}"}


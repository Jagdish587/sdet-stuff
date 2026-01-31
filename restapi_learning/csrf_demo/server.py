from fastapi import FastAPI, Request, Response, Header, HTTPException
import uuid

app = FastAPI()

# In-memory session store
sessions = {}

@app.get("/login")
def login(response: Response):
    session_id = str(uuid.uuid4())
    csrf_token = str(uuid.uuid4())

    sessions[session_id] = {
        "user": "alice",
        "csrf": csrf_token
    }

    response.set_cookie("session_id", session_id)
    return {
        "message": "logged in",
        "csrf_token": csrf_token
    }


@app.post("/transfer")
def transfer(
    request: Request,
    x_csrf_token: str = Header(None)
):
    session_id = request.cookies.get("session_id")
    session = sessions.get(session_id)

    if not session:
        raise HTTPException(401, "Not logged in")

    if x_csrf_token != session["csrf"]:
        raise HTTPException(403, "CSRF validation failed")

    return {"status": "money transferred "}


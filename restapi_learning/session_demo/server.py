from fastapi import FastAPI, Response, Request
import uuid

app = FastAPI()

# Server-side session store (in-memory)
sessions = {}

@app.get("/login")
def login(response: Response):
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"user": "alice"}

    # Store only session ID in cookie
    response.set_cookie(
        key="session_id",
        value=session_id
    )
    return {"message": "logged in", "session_id": session_id}

@app.get("/profile")
def profile(request: Request):
    session_id = request.cookies.get("session_id")
    session = sessions.get(session_id)

    if not session:
        return {"error": "not logged in"}

    return {"message": f"hello {session['user']}"}


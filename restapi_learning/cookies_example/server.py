from fastapi import FastAPI, Response, Request

app = FastAPI()

@app.get("/login")
def login(response: Response):
    response.set_cookie(key="user", value="alice")
    return {"message": "logged in"}

@app.get("/profile")
def profile(request: Request):
    user = request.cookies.get("user")
    if not user:
        return {"error": "not logged in"}
    return {"message": f"hello {user}"}


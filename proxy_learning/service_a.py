from fastapi import FastAPI

app = FastAPI()

@app.get("/{path:path}")
def service_a(path: str):
    return {
        "service": "A",
        "path": path
    }


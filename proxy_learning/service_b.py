from fastapi import FastAPI

app = FastAPI()

@app.get("/{path:path}")
def service_b(path: str):
    return {
        "service": "B",
        "path": path
    }


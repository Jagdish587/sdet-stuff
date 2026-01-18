from flask import Flask, jsonify, request
import time
import random
import uuid

app = Flask(__name__)

# Fake in-memory storage
USERS = []
TOKENS = set()

@app.route("/")
def home():
    return "Welcome to Locust Test App 🚀"

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    # Very simple login check
    if data.get("username") == "admin" and data.get("password") == "secret":
        token = str(uuid.uuid4())
        TOKENS.add(token)
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/api/users", methods=["GET", "POST"])
def users():
    # Check auth token
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header not in TOKENS:
        return jsonify({"error": "Unauthorized"}), 401

    # Simulate processing delay
    time.sleep(random.uniform(0.1, 0.4))

    if request.method == "POST":
        user = request.json
        USERS.append(user)
        return jsonify({"message": "User created", "user": user}), 201

    return jsonify({"users": USERS})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

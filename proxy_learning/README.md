# Reverse Proxy Example with FastAPI

This project demonstrates a simple reverse proxy implementation using FastAPI and HTTPX. It consists of a proxy service that routes requests to two backend services (Service A and Service B).

## Prerequisites
- Python 3.7+

## Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip3 install fastapi uvicorn requests python-jose httpx
   ```

## Usage

You will need to run each service in a separate terminal window. Ensure you have the virtual environment activated in each terminal.

### 1. Start Service A
Runs on port **9001**.
```bash
uvicorn service_a:app --port 9001
```

### 2. Start Service B
Runs on port **9002**.
```bash
uvicorn service_b:app --port 9002
```

### 3. Start Reverse Proxy
Runs on port **8000**.
```bash
uvicorn reverse_proxy:app --port 8000
```

## Testing the Proxy

Once all services are running, you can test the reverse proxy using `curl` or a web browser.

**Access Service A via Proxy:**
```bash
curl http://localhost:8000/service-a/hello
```
*Expected Output:* `{"service":"A", "path":"hello"}`

**Access Service B via Proxy:**
```bash
curl http://localhost:8000/service-b/foo/bar
```
*Expected Output:* `{"service":"B", "path":"foo/bar"}`

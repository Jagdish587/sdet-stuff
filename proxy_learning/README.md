## reverse proxy examples

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install fastapi uvicorn requests python-jose httpx 

Run the Services
Start Service A
uvicorn service_a:app --port 9001

Start Reverse Proxy
uvicorn reverse_proxy:app --port 8000

Test the APIs
1. Service A – Hello Endpoint
curl http://localhost:8000/service-a/hello

2. Service B – Foo/Bar Endpoint
curl http://localhost:8000/service-b/foo/bar

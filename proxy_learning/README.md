
### This is example for reverse proxy

python3 -m venv venv 
source venv/bin/activate 
pip3 install fastapi uvicorn requests python-jose httpx 
** from termianl**
uvicorn service_a:app --port 9001  
uvicorn service_a:app --port 9001 
uvicorn reverse_proxy:app --port 8000 

(1) curl http://localhost:8000/service-a/hello 

(2) curl http://localhost:8000/service-b/foo/bar

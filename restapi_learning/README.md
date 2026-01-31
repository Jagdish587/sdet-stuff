## install dependencies
python3 -m venv venv  
source venv/bin/activate  
pip3 install fastapi uvicorn requests python-jose 


### running server and client
uvicorn server:app --reload  
python3 client.py 

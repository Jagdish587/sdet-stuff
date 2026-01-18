### steps
python3 -m venv venv
source venv/bin/activate
pip install locust
pip install flask

steps 
======
`locust --version` 
 From terminal 1 , run python app.py , open `http://127.0.0.1:5000` 
 From termminal 2, run locust, will open GUI `http://0.0.0.0:8089/` 
 For headless case , run  
`locust --headless -u 10 -r 2 --host http://localhost:5000`
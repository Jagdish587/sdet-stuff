import socket

HOST = "10.69.214.106"
PORT = 9091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    print("Connecting to:", HOST)
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print("Received:", data.decode())
except Exception as e:
    print("Connection failed:", e)
finally:
    s.close()


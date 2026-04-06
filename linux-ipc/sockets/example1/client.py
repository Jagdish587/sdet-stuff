import socket

client = socket.socket()
client.connect(("localhost", 5000))

client.send(b"Hello from client")

data = client.recv(1024)
print("Server says:", data.decode())

client.close()

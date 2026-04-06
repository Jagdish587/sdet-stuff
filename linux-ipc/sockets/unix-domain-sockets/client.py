import socket

socket_path = "/tmp/mysocket"

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(socket_path)

client.send(b"Hello from client")

data = client.recv(1024)
print("Server says:", data.decode())

client.close()

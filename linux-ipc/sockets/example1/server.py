import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024)
print("Received:", data.decode())

conn.send(b"Hello from server")

conn.close()

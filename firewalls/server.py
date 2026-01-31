import socket

HOST = "0.0.0.0"
PORT = 9091

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f"Listening on port {PORT}...")

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    conn.sendall(b"Hello from server\n")
    conn.close()


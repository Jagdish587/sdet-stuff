import socket
import ssl

HOST = "0.0.0.0"
PORT = 8443

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"TLS Server listening on {HOST}:{PORT}")

# Create TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Wrap TCP socket with TLS
    tls_socket = context.wrap_socket(client_socket, server_side=True)

    # Receive HTTP request (encrypted over TLS)
    request = tls_socket.recv(1024).decode()
    print("Received request:")
    print(request)

    # Send HTTP response
    response = """HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 12

Hello TLS!
"""
    tls_socket.sendall(response.encode())

    tls_socket.close()
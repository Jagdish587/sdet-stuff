import socket
import ssl

HOST = "0.0.0.0"
PORT = 8443

# TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("mTLS Server running...")

# TLS context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Require client certificate
context.load_verify_locations(cafile="ca.crt")
context.verify_mode = ssl.CERT_REQUIRED

while True:
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    tls_socket = context.wrap_socket(client_socket, server_side=True)

    # Verify client cert
    client_cert = tls_socket.getpeercert()
    print("Client cert:", client_cert)

    request = tls_socket.recv(1024).decode()
    print("Request:", request)

    response = """HTTP/1.1 200 OK
Content-Length: 11

Hello mTLS!
"""
    tls_socket.sendall(response.encode())
    tls_socket.close()
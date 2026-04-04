import socket
import ssl

HOST = "127.0.0.1"
PORT = 8443

# TCP connection
sock = socket.create_connection((HOST, PORT))

# TLS context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Load client cert (THIS is what makes it mTLS)
context.load_cert_chain(certfile="client.crt", keyfile="client.key")

# Trust CA
context.load_verify_locations(cafile="ca.crt")

tls_socket = context.wrap_socket(sock, server_hostname="localhost")

# Send request
request = """GET / HTTP/1.1
Host: localhost

"""
tls_socket.sendall(request.encode())

response = tls_socket.recv(4096).decode()
print(response)

tls_socket.close()
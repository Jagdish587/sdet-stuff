import socket
import ssl

HOST = "127.0.0.1"
PORT = 8443

# Create TCP connection
sock = socket.create_connection((HOST, PORT))

# Create TLS context
context = ssl.create_default_context()

# (For self-signed cert — disable verification for demo)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Wrap socket with TLS
tls_socket = context.wrap_socket(sock, server_hostname=HOST)

# Send HTTP request
request = """GET / HTTP/1.1
Host: localhost

"""
tls_socket.sendall(request.encode())

# Receive response
response = tls_socket.recv(4096).decode()
print("Server response:")
print(response)

tls_socket.close()
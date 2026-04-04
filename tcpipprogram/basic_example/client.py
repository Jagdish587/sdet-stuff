import socket

HOST = "127.0.0.1"
PORT = 8080

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

# Send HTTP request
request = """GET / HTTP/1.1
Host: localhost

"""

client_socket.sendall(request.encode())

# Receive response
response = client_socket.recv(4096).decode()
print("Server response:")
print(response)

# Close socket
client_socket.close()
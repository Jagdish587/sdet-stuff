import socket

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 8080

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address
server_socket.bind((HOST, PORT))

# Start listening
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive request
    request = client_socket.recv(1024).decode()
    print("Received request:")
    print(request)

    # Create HTTP response
    response = """HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 13

Hello, World!
"""

    # Send response
    client_socket.sendall(response.encode())

    # Close connection
    client_socket.close()
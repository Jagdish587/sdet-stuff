# 1. Create CA
openssl req -x509 -newkey rsa:2048 -keyout ca.key -out ca.crt -days 365 -nodes

# 2. Server cert
openssl req -newkey rsa:2048 -keyout server.key -out server.csr -nodes
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -out server.crt -days 365

# 3. Client cert
openssl req -newkey rsa:2048 -keyout client.key -out client.csr -nodes
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -out client.crt -days 365



1. TCP handshake

2. TLS handshake:
   ClientHello
   ServerHello + Certificate
   Server requests client certificate
   Client sends certificate
   Both verify each other
   Secure channel established
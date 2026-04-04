### How to Run
Step 1: Start server 
python server_tls.py
Step 2: Run client 
python client_tls.py

### 
TLS needs a certificate.

Run this once:
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

This creates:

cert.pem (certificate)
key.pem (private key)

### Flow mechanism
1. TCP handshake
   SYN → SYN-ACK → ACK

2. TLS handshake
   ClientHello
   ServerHello + Certificate
   Key exchange
   Secure channel established

3. HTTP over TLS
   Encrypted request/response
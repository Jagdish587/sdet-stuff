###
A Unix Domain Socket (UDS) is a socket used for communication within the same machine, 
using a file path instead of IP/port.

###
🧠 Simple Analogy
TCP socket → calling over the internet 🌐
Unix socket → talking inside the same room 🏠

###
🔑 Key Features
✔ Works only on same machine
✔ Uses file path (e.g., /tmp/mysocket)
✔ Faster than network sockets
✔ Supports bidirectional communication

👉 Faster than TCP sockets (no network stack overhead)
### UDS vs TCP Socket
| Feature  | Unix Socket | TCP Socket |
| -------- | ----------- | ---------- |
| Scope    | Local only  | Network    |
| Speed    | 🚀 Faster   | Slower     |
| Address  | File path   | IP + Port  |
| Overhead | Low         | Higher     |

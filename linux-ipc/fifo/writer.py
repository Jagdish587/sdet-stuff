import os

fifo_path = "myfifo"

# Create FIFO if it doesn't exist
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open(fifo_path, "w") as fifo:
    fifo.write("Hello from writer process!\n")

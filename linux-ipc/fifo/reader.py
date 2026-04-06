fifo_path = "myfifo"

with open(fifo_path, "r") as fifo:
    msg = fifo.read()
    print("Reader received:", msg)

import mmap
import time

FILE_SIZE = 1024

# Create file with fixed size
with open("logfile.txt", "wb") as f:
    f.write(b"\x00" * FILE_SIZE)

with open("logfile.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), FILE_SIZE)

    for i in range(5):
        message = f"Log {i}\n".encode()
        mm.seek(0)
        mm.write(message)

        print("Writer wrote:", message.decode().strip())
        time.sleep(2)

    mm.close()

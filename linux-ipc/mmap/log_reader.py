import mmap
import time

FILE_SIZE = 1024

with open("logfile.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), FILE_SIZE)

    while True:
        mm.seek(0)
        data = mm.readline()

        if data:
            print("Reader saw:", data.decode().strip())

        time.sleep(1)

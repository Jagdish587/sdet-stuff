from multiprocessing import shared_memory

# Attach to existing shared memory (name must match)
shm = shared_memory.SharedMemory(name="psm_XXXXXX")  # replace with actual name

data = bytes(shm.buf[:11])
print("Reader got:", data.decode())

shm.close()

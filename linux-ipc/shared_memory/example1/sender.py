from multiprocessing import Process, shared_memory

def writer():
    shm = shared_memory.SharedMemory(create=True, size=100)
    shm.buf[:11] = b"Hello World"
    
    print("Writer wrote data")
    input("Press Enter after reader finishes...")  # keep alive
    
    shm.close()
    shm.unlink()

if __name__ == "__main__":
    writer()

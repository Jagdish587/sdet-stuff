from multiprocessing import Process, Event, shared_memory

def writer(event, shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    
    print("Writer writing...")
    shm.buf[:11] = b"Hello World"
    
    event.set()  # 🔔 signal that writing is done
    
    shm.close()

def reader(event, shm_name):
    print("Reader waiting...")
    
    event.wait()  # ⏳ wait until writer signals
    
    shm = shared_memory.SharedMemory(name=shm_name)
    data = bytes(shm.buf[:11])
    
    print("Reader got:", data.decode())
    
    shm.close()

if __name__ == "__main__":
    event = Event()
    
    shm = shared_memory.SharedMemory(create=True, size=100)
    
    p1 = Process(target=writer, args=(event, shm.name))
    p2 = Process(target=reader, args=(event, shm.name))
    
    p2.start()  # start reader first (safe now!)
    p1.start()
    
    p1.join()
    p2.join()
    
    shm.close()
    shm.unlink()

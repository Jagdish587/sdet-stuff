from multiprocessing import Process, Event, shared_memory
import time

def producer(data_ready, space_ready, shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)
    
    messages = [b"Hello", b"World", b"Shared", b"Memory"]

    for msg in messages:
        space_ready.wait()      # wait until buffer is free
        space_ready.clear()

        print("Producer writing:", msg)
        shm.buf[:len(msg)] = msg

        data_ready.set()        # signal data is ready

    shm.close()


def consumer(data_ready, space_ready, shm_name):
    shm = shared_memory.SharedMemory(name=shm_name)

    for _ in range(4):
        data_ready.wait()       # wait for producer
        data_ready.clear()

        data = bytes(shm.buf[:20]).rstrip(b'\x00')
        print("Consumer read:", data.decode())

        space_ready.set()       # signal buffer is free

    shm.close()


if __name__ == "__main__":
    data_ready = Event()
    space_ready = Event()

    space_ready.set()  # initially buffer is empty → producer can write

    shm = shared_memory.SharedMemory(create=True, size=100)

    p = Process(target=producer, args=(data_ready, space_ready, shm.name))
    c = Process(target=consumer, args=(data_ready, space_ready, shm.name))

    c.start()
    p.start()

    p.join()
    c.join()

    shm.close()
    shm.unlink()

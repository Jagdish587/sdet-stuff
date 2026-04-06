from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increment, args=(counter, lock))
    p2 = Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final counter:", counter.value)

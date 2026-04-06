from multiprocessing import Process, Lock
import time

def task1(lock1, lock2):
    print("Task1 acquiring lock1...")
    lock1.acquire()
    time.sleep(1)

    print("Task1 acquiring lock2...")
    lock2.acquire()

    print("Task1 running...")
    lock2.release()
    lock1.release()

def task2(lock1, lock2):
    print("Task2 acquiring lock2...")
    lock2.acquire()
    time.sleep(1)

    print("Task2 acquiring lock1...")
    lock1.acquire()

    print("Task2 running...")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    p1 = Process(target=task1, args=(lock1, lock2))
    p2 = Process(target=task2, args=(lock1, lock2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

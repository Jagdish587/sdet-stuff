import threading

num = 0

even_event = threading.Event()
odd_event = threading.Event()

even_event.set()   # even starts first
odd_event.clear()  # odd waits

def print_even():
    global num
    while num <= 20:
        even_event.wait()   # wait until allowed

        if num <= 20:
            print("Even:", num)
            num += 1

        even_event.clear()  # block even
        odd_event.set()     # allow odd


def print_odd():
    global num
    while num <= 20:
        odd_event.wait()    # wait until allowed

        if num <= 20:
            print("Odd :", num)
            num += 1

        odd_event.clear()   # block odd
        even_event.set()    # allow even


t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()

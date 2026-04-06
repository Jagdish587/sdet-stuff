from multiprocessing import Process, Pipe
"""
What’s Happening Here ..??
Pipe() creates two ends of a pipe:
parent_conn → used by parent
child_conn → used by child
Parent sends: "Hello from parent!"
Child receives and prints it
"""

def child_process(conn):
    msg = conn.recv()   # receive message from pipe
    print("Child received:", msg)
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p = Process(target=child_process, args=(child_conn,))
    p.start()

    parent_conn.send("Hello from parent!")  # send message
    parent_conn.close()

    p.join()

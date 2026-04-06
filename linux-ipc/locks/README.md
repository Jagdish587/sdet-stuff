### 
If multiple processes modify shared data → ALWAYS use synchronization (Lock/Semaphore)

###
with lock: is just a safer wrapper around
lock.acquire() and lock.release()

### These two are the same:
```python
lock.acquire()
try:
    counter.value += 1
finally:
    lock.release()
```

```python
with lock:
    counter.value += 1
```


### When to Use acquire() / release() ???
Use manual control when:

You need fine-grained control
You want timeout handling:
lock.acquire(timeout=2)

###
Deadlock occurs when processes hold resources and wait for each other in a circular chain.
Deadlock = circular waiting between processes holding locks

###
✅ Fix #1: Consistent Lock Ordering

👉 Always acquire locks in same order

def task(lock1, lock2):
    with lock1:
        time.sleep(1)
        with lock2:
            print("Safe execution")
👉 Both processes follow:

lock1 → lock2

✔ No circular wait
✔ No deadlock


✅ Fix #2: Timeout (Advanced)
if lock.acquire(timeout=2):
    # try work

👉 Avoids infinite waiting
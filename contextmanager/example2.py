from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()          # setup
    yield                        # control goes to with-block
    end = time.time()            # cleanup
    print(f"Time taken: {end - start:.4f} seconds")

# Using it
with timer():
    total = sum(range(1000000))

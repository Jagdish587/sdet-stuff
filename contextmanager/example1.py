from contextlib import contextmanager

@contextmanager
def my_context():
    print("Start")
    yield
    print("End")

with my_context():
    print("Inside")

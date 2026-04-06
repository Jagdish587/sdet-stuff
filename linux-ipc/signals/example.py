import signal
import time

def handler(signum, frame):
    print(f"Received signal: {signum}")

# Register handler
signal.signal(signal.SIGINT, handler)

print("Running... Press Ctrl+C")

while True:
    time.sleep(1)

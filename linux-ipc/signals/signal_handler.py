import signal
import time
import sys

running = True

def shutdown_handler(signum, frame):
    global running
    print(f"\nReceived signal {signum}. Shutting down gracefully...")
    running = False

# Register signals
signal.signal(signal.SIGINT, shutdown_handler)   # Ctrl+C
signal.signal(signal.SIGTERM, shutdown_handler)  # kill command

def main():
    print("Process started. Press Ctrl+C to stop.")

    while running:
        print("Working...")
        time.sleep(2)

    # Cleanup section
    print("Cleaning up resources...")
    time.sleep(1)

    print("Shutdown complete.")
    sys.exit(0)

if __name__ == "__main__":
    main()

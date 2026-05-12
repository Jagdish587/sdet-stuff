from contextlib import contextmanager

@contextmanager
def open_file(filename, mode="w"):
    file = open(filename, mode)
    print(f"File '{filename}' opened")
    try:
        yield file
    finally:
        file.close()
        print(f"File '{filename}' closed automatically")


# --- main ---
filename = input("Enter filename: ")

with open_file(filename, "w") as f:
    f.write("Hello, World!\n")
    f.write("Written from main block.\n")
    print("Writing done in main")

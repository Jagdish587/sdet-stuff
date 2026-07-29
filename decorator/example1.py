def decorator_func(main_func):
    def wrapper_func():
        val = main_func()
        val += 10
        return val
    return wrapper_func

@decorator_func
def main_func():
    return 5

print(main_func()) # o/p 15

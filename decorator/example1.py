def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

def my_decorator(func):

    def wrapper(a, b):
        print("Adding two numbers...")
        result = func(a, b)
        print("Result is:", result)
        return result

    return wrapper


@my_decorator # add = my_decorator(add), returns wrapper
def add(a, b):
    return a + b


val = add(10, 20) # calls wrapper(10, 20)
print("val = ", val)
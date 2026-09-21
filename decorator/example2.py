def mydecorator_func(myactual_func):
    def inner_func():
        print("entered inside decorator func")
        return myactual_func()

    return inner_func


@mydecorator_func
def my_func():
    print("entered inside actual func")


my_func()
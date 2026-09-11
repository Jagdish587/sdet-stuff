def mydecorator_func(myactaul_func):
  def inner_func():
    print("entered inside decorator func")
    return myactaul_func

@mydecorator_func
def my_func():
  print("entered inside actual func")


my_func()


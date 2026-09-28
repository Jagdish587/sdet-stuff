def test():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")


x = test() # func does not gets called here
print("after x")
print(next(x)) # 10
print(next(x)) 20

"""
o/p:
after x
Start
10
Middle
20

"""

class BaseClass:
    def __init__(self):
        print("base class constructor")
    def display(self):
        print("base class display")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("derived class constructor")
    def display(self):
        super().display()
        print("derived class display")

my_obj = DerivedClass()
my_obj.display()

"""
o/p:
base class constructor
derived class constructor
base class display
derived class display
"""
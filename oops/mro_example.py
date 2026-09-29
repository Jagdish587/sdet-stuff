


"""
      A
     / \
    B   C
     \ /
      D
"""

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.show() # prints B


print(D.mro())
print(D.__mro__) # same o/p for both
"""
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

"""




class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


obj = D()
obj.show()
"""
D
B
C
A
"""
super() follows the MRO and continues the method lookup from the next class.
D → B → C → A → object
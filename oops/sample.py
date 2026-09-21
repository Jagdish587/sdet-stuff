from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.__name = name          # Encapsulation

    def get_name(self):
        return self.__name

    @abstractmethod                # Abstraction
    def sound(self):
        pass


class Dog(Animal):                 # Inheritance
    # Method Overriding
    def sound(self):
        print("Bark")


class Cat(Animal):                 # Inheritance
    # Method Overriding
    def sound(self):
        print("Meow")


# Create objects
dog = Dog("Tommy")
cat = Cat("Kitty")


# Polymorphism
# Method overriding is a technique. 
# Polymorphism is a concept/behavior.
# Polymorphism is an OOP concept where the same interface or method can have different implementations or behaviors 
# depending on the object using it
animals = [dog, cat]

for animal in animals:
    animal.sound()

"""
Concept	Where?	What is happening?
Encapsulation	__name	Name is protected inside the class
Inheritance	Dog(Animal)	Dog gets functionality from Animal
Polymorphism	animal.sound()	Dog and Cat produce different sounds
Abstraction	@abstractmethod	Animal defines what sound() must exist, not how it works
"""


class Calculator:
    # method over loading, 
    def add(self, a, b, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(2, 3))       # 5
print(obj.add(2, 3, 4))    # 9

"""
Method Overloading in Python

Method overloading means having multiple methods with the same name but different parameters.

Unlike Java or C++, Python does not support traditional method overloading directly. If you define multiple methods with the same name, 
the last definition replaces the previous ones.
"""

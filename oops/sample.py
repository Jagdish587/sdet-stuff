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

    def sound(self):
        print("Bark")


class Cat(Animal):                 # Inheritance

    def sound(self):
        print("Meow")


# Create objects
dog = Dog("Tommy")
cat = Cat("Kitty")


# Polymorphism
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
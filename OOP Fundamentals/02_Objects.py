# Object creation in python happens generally through constructors, that is when an object is created the class
# calls __new__ method to allocate memory and then the object calls __init__ method to initialize the default variable


#when using dataclass, it is more clean
from dataclasses import dataclass

class Animal:
    __name: str
    __says: str
    __weight: float
    def __init__(self, name: str, says: str, weight: float):
        self.__name = name
        self.__says = says
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def says(self):
        return self.__says

    @property
    def weight(self):
        return self.__weight

    @name.setter
    def name(self, value: str):
        self.__name = value

    @says.setter
    def says(self, value: str):
        self.__says = value

    @weight.setter
    def weight(self, value: float):
        self.__weight = value

@dataclass
class Animal2:
    __name: str
    __says: str
    __weight: float

if __name__ == "__main__":
    animal = Animal("cow", "moo", 45.65)
    print(animal.name)
    print(animal.says)
    print(animal.weight)

    animal2 = Animal2("Dog", "Barks", 23.12)
    print(animal2.__dict__["_Animal2__name"])
    print(animal2.__dict__["_Animal2__says"])
    print(animal2.__dict__["_Animal2__weight"])

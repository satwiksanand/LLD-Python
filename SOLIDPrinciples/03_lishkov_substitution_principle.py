# If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering
# any of the desirable properties of that program (correctness, task performed, etc.).
from abc import ABC, abstractmethod


# Bad Example: a square is a rectangle
class BadRectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

class BadSquare(BadRectangle):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def set_width(self, width):
        self._width = width
        self._height = width

    def set_height(self, height):
        self._width = height
        self._height = height

# even though mathematically square is a rectangle, the above code fails
rect = BadSquare(5, 5)
rect.set_height(10)
rect.set_width(20)

print(f"rectangle area: {rect.area()}") # should have been 200 but is 400

# as we can see square can not be substituted in place of rectangle as it shows unusual behavior

# Good Example
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width * self._height)

class Square(Shape):
    def __init__(self, side: int):
        self._side = side

    def area(self):
        return self._side * self._side

    def perimeter(self):
        return 4 * self._side

def print_shape_details(shape: Shape):
    print(f"shape details:\n{{area: {shape.area()}}}\n{{perimeter: {shape.perimeter()}}}")

shape = Rectangle(20, 10)
print_shape_details(shape)
shape = Square(10)
print_shape_details(shape)


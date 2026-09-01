# A mechanism where a new object automatically acquires the properties and behaviors of an existing object.
# This establishes a hierarchical relationship and promotes immense reusability,
# allowing the new object to build upon existing foundations rather than starting from scratch.

class Car:
    def __init__(self, wheels: int, max_speed: int, num_of_seats: int):
        self._wheels = wheels
        self._max_speed = max_speed
        self._num_of_seats = num_of_seats

    def move_forward(self):
        print("moving forward...")

    def accelerate(self):
        print("accelerating...")

    def stop(self):
        print("stopping the car...")

class DieselCar(Car):
    def __init__(self, wheels: int, max_speed: int, num_of_seats: int, mileage: int):
        super().__init__(wheels, max_speed, num_of_seats)
        self._mileage = mileage

    @property
    def mileage(self):
        return self._mileage

class ElectricCar(Car):
    def __init__(self, wheels: int, max_speed: int, num_of_seats: int):
        super().__init__(wheels, max_speed, num_of_seats)

    def open_door(self):
        print("opening door...")

if __name__ == "__main__":
    car = ElectricCar(4, 300, 4)
    car.move_forward()
    car.accelerate()
    car.stop()
    car.open_door()

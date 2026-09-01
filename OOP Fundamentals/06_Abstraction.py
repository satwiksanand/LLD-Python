#The process of hiding the complex, underlying implementation details of a system and exposing only the essential,
# high-level interface to the user. It reduces complexity by allowing you to use a feature
# without understanding how it is built.
from time import sleep

class ResourceError(Exception):
    pass

class CoffeeMachine:
    def __init__(self, water_level: int, beans_level: int):
        self.__water_level = water_level
        self.__beans_level = beans_level

    def _heat_water(self):
        if self.__water_level < 30:
            raise ResourceError("Not Enough Water")
        print("heating water...")
        sleep(1)

    def _grind_beans(self):
        if self.__beans_level < 10:
            raise ResourceError("Not Enough Beans")
        print("grinding beans...")
        sleep(1)

    def _regulating_pressure(self):
        print("regulating pressure")
        sleep(1)

    def make_espresso(self):
        # this functions acts as an orchestrator and manager the control flow of the function.
        try:
            self._heat_water()
            self._grind_beans()
            self._regulating_pressure()
            print("espresso ready")
            self.__water_level -= 30
            self.__beans_level -= 10
        except ResourceError as err:
            print(err)

    ## getters and setters for private variables.
    @property
    def water_level(self):
        return self.__water_level

    @property
    def beans_level(self):
        return self.__beans_level

    @water_level.setter
    def water_level(self, value):
        # we are adding water to the coffee machine
        self.__water_level += value

    @beans_level.setter
    def beans_level(self, value):
        # we are adding beans to the coffee machine
        self.__beans_level += value

if __name__ == "__main__":
    machine = CoffeeMachine(10, 100)
    machine.make_espresso()
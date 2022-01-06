from homework_02.base import Vehicle
from homework_02.exceptions import *


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, number):
        if self.cargo + number <= self.max_cargo:
            self.cargo += number
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result

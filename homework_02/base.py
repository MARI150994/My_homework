from abc import ABC
from homework_02.exceptions import *


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        possible_distance = self.fuel // self.fuel_consumption
        if possible_distance < distance:
            raise NotEnoughFuel
        else:
            self.fuel -= self.fuel_consumption * distance

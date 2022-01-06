class LowFuelError(Exception):
    def __init__(self):
        super().__init__(f'Not enough fuel to start')


class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__(f'Not enough fuel for the given distance')


class CargoOverload(Exception):
    def __init__(self):
        super().__init__(f'Permissible cargo exceeded')

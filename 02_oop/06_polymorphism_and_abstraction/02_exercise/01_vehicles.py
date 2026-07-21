from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_FUEL_CONSUMPTION = 0.9

    def drive(self, distance: int):
        needed_fuel = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if needed_fuel < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL_CONSUMPTION = 1.6
    REFUEL_MAXIMUM = 0.95

    def drive(self, distance: int):
        needed_fuel = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if needed_fuel < self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.REFUEL_MAXIMUM


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
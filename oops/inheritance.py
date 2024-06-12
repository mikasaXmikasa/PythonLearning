class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_capacity = 0

    def update_gas_tank_capacity(self, gas_tank_capacity):
        """Updates the gas tank capacity of the car"""
        self.gas_tank_capacity = gas_tank_capacity

    def fill_gas_tank(self, amount):
        """Fill the gas tank by given amount extra will overflow"""
        print(f"Printing the {gas_tank_capacity} gas tank")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    
class Battery:
    def __init__(self, battery_size=40):
        """Initilize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-KWH battery.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn'thave a gas tank")

    def update_gas_tank_capacity(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn'thave a gas tank")

my_leaf = ElectricCar("Nissan", "Leaf", 2024)
my_leaf.get_descriptive_name()
my_leaf.fill_gas_tank()
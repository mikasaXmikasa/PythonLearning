class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        print(f"{self.make.title()} {self.model.upper()} {self.year}")

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value
        Reject the change if it attempts to roll odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer.")

    def increment_odometer(self, miles):
        """Add the given amountn to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print(f"Cannot update using negative value of {miles}")
car1 = Car("Audi", "A4", 2003)
car1.get_descriptive_name()
car1.read_odometer()


# Modifying attribute values

#1. Using setter function 2. directly using instance 3. increment using a method

car1.update_odometer(30)
car1.read_odometer()


car1.update_odometer(20)


car1.increment_odometer(-2)
car1.increment_odometer(10)
car1.read_odometer()
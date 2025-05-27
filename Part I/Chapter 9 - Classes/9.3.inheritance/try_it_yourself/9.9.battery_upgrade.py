"""
9-9. Battery Upgrade:

• Use the final version of electric_car.py from this section.

• Add a method to the Battery class called upgrade_battery().

• This method should check the battery size and set the capacity to 100
    if it isn’t already.

• Make an electric car with
    • a default battery size,
    • call get_range() once,
    • and then call get_range() a second time after upgrading the battery.

• You should see an increase in the car’s range.
"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Gather descriptive characteristics of a car into a string"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Ad the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attemp to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        car_range = 0
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        print(f"This car can go about {car_range} miles on a full charge.")

    def upgrade_battery(self):
        """
        Check if the battery size is lower than 100-kWh, upgrades to 100-kWh.
        """
        if self.battery_size < 100:
            self.battery_size = 100
            message =f"\nThe battery size has been upgraded to "
            message += f"{self.battery_size}-kWh.\n"
            print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


electric_car = ElectricCar('byd', 'shark', 2026)

electric_car.battery.describe_battery()
electric_car.battery.get_range()

electric_car.battery.upgrade_battery()

electric_car.battery.describe_battery()
electric_car.battery.get_range()

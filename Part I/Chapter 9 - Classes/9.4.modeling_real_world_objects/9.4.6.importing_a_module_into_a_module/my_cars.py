from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2025)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2025)
print(my_tesla.get_descriptive_name())
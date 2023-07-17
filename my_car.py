'''导入一个Car类的模块——car.py'''

from car import Car, ElectricCar

my_beetle_car = Car('volkswagen','beetle','2016') # 实例化一个车
print(my_beetle_car.get_descriptive_name())

my_tesla_car = Car('Tesla','roadster','2016') # 实例化一个车
print(my_tesla_car.get_descriptive_name())
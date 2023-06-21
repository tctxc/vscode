class Car():
    '''这是一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year) -> None:
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印一条指出汽车里程的信息'''
        print('This car has '+ str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self,mileage):
        '''将里程表读数设置为指定的值
        方法update_odometer()位于类Car中，共享同一个命名空间，
        可以通过self方位到其他方法中的属性
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incremeter_odometer(self, miles):
        '''将里程表读数增加指定的量'''
        self.odometer_reading += miles



my_new_car = Car('audi','a4','2016') # 实例化一个车
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
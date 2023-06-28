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

class Battery():
    def __init__(self,battery_size) -> None:
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''打印一条描述电池容量的信息'''
        print('\nThis car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        else:
            self.battery_size == 85
            range = 270

        message = "This car can go approximately " + str(range) + 'miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            self.battery_size =85


class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self, make, model, year):
        '''
        初始化父类的属性
        同时初始化电动车子类自己的特有属性
        使子类具有自己的独特之处
        '''
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.get_range()
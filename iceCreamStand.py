class Restaurant():
    '''定义了一个餐厅的类，包含描述餐厅名字和菜系的方法，餐厅还能营业，和顾客打招呼'''
    def __init__(self, restaurant_name, cuisine_type) -> None:
        '''初始化餐厅名称和菜品风格'''
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''展示餐厅的名称'''
        print('\n有一家新开的餐厅: '+ self.name)
        print('菜系是：'+ self.cuisine)

    def open_restaurant(self, customer):
        '''展示餐厅的工作状态'''
        print('餐厅正在营业！')
        print('欢迎光临!')
        customer.greet_user()

    def served_number(self):
        '''打印出有多少人在餐厅就餐过'''
        print(f'\n{self.number_served}人在餐厅就餐过。')
    
    def set_number_served(self, quantity):
        '''设置餐厅就餐的人数，且就餐人数不应为负值'''
        if quantity >= 0:
            self.number_served = quantity
        else:
            print('就餐人数不能低于0！')

    def increment_number_served(self, amount):
        '''将就餐人数增加指定的量'''
        self.number_served += amount


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['芒果冰', '草莓冰', '香草冰','撞色冰']

    def describe_icecreamstand(self):
        super().describe_restaurant()
        print('今日主打口味：')
        print(self.flavors)
        # return super().describe_restaurant()

ice_cream = IceCreamStand('冰淇凌小店', '夏日甜品')
ice_cream.describe_icecreamstand()
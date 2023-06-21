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



class User():
    '''定义了一个顾客的类'''
    def __init__(self, first_name, last_name, age, sex, login_attempts) -> None:
        self.f_name = first_name
        self.l_name = last_name
        self.user_age = age
        self.user_sex = sex
        self.count = login_attempts
        pass

    def describe_user(self):
        print('顾客：'+ self.l_name + self.f_name + '简介')
        print('\n年龄： '+ str(self.user_age))
        print('\n性别： '+ self.user_sex)
        print('\n登录次数： '+ str(self.count))

    def greet_user(self):
        print('Hello! '+ self.l_name + self.f_name + '!')

    def increment_login_attempts(self):
        self.count += 1
        print(self.count)

    def reset_login_attempts(self):
        self.count = 0
        print(self.count)
    



'''实例化三个餐厅'''
jianghurenjia = Restaurant('江湖人家', '川菜')
qiaojiangnan = Restaurant('俏江南', '杭州菜')
dingshunlai = Restaurant('鼎顺来', '烧烤')

'''实例化一个顾客'''
tctxc = User('tiancai','tang', 22, '男生',3)

'''对顾客类实例化后，进行了一些操作'''
tctxc.describe_user()
tctxc.increment_login_attempts()
tctxc.increment_login_attempts()
tctxc.reset_login_attempts()



jianghurenjia.describe_restaurant()
jianghurenjia.open_restaurant(tctxc)

jianghurenjia.set_number_served(200)
jianghurenjia.served_number()

jianghurenjia.increment_number_served(100)
jianghurenjia.served_number()

# tctxc.describe_user()
# tctxc.greet_user()


# qiaojiangnan.describe_restaurant()
# qiaojiangnan.open_restaurant()

# dingshunlai.describe_restaurant()
# dingshunlai.open_restaurant()

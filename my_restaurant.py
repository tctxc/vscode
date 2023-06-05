class Restaurant():
    '''定义了一个餐厅的类，包含描述餐厅名字和菜系的方法，餐厅还能营业，和顾客打招呼'''
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('\n有一家新开的餐厅: '+ self.name)
        print('菜系是：'+ self.cuisine)

    def open_restaurant(self, customer):
        print('餐厅正在营业！')
        print('欢迎光临!')
        customer.greet_user()

class User():
    '''定义了一个顾客的类'''
    def __init__(self, first_name, last_name, age, sex) -> None:
        self.f_name = first_name
        self.l_name = last_name
        self.user_age = age
        self.user_sex = sex
        pass

    def describe_user(self):
        print('顾客：'+ self.l_name + self.f_name + '简介')
        print('\n年龄： '+ str(self.user_age))
        print('\n性别： '+ self.user_sex)

    def greet_user(self):
        print('Hello! '+ self.l_name + self.f_name + '!')



'''实例化三个餐厅'''
jianghurenjia = Restaurant('江湖人家', '川菜')
qiaojiangnan = Restaurant('俏江南', '杭州菜')
dingshunlai = Restaurant('鼎顺来', '烧烤')

'''实例化一个顾客'''
tctxc = User('tiancai','tang', 22, '男生')

jianghurenjia.describe_restaurant()
jianghurenjia.open_restaurant(tctxc)
# tctxc.describe_user()
# tctxc.greet_user()


# qiaojiangnan.describe_restaurant()
# qiaojiangnan.open_restaurant()

# dingshunlai.describe_restaurant()
# dingshunlai.open_restaurant()



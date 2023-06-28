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

class Privileges():
    def __init__(self, *privileges) -> None:
        '''*privileges是一个特殊的参数形式，称为可变位置参数。它表示函数可以接受任意数量的参数，并将它们保存在一个元组中。'''
        self.privileges = privileges

    def show_privileges(self):
        print('\nAdmin has some privileges such are: ') #使用加号连接时，必须是str
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    '''
    由用户类下推/继承出一个管理员用户
    管理员用户具有一定的特权
    '''
    def __init__(self, first_name, last_name, age, sex) -> None:
        super().__init__(first_name, last_name, age, sex)
        # 一个类的构造函数中调用了其他的类
        self.privileges = Privileges() #Admin类的构造函数中，将它初始化为一个Privileges对象，因此admin.privileges是一个Privileges类型的对象。



admin = Admin('asuka', 'li', 18, 'shemale')

admin.privileges.privileges = ['can add post', 'can del post', 'can ban user']
# admin.privileges是一个Privileges类型的对象。
# 接着，.privileges访问了Privileges对象的privileges属性，将其设为了一个列表['can add post', 'can del post', 'can ban user']。
# 这个列表包含了管理员的特权信息。

admin.privileges.show_privileges()
# admin.privileges是一个Privileges类型的对象。
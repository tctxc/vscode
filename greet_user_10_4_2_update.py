import json
import os

def get_username():
    '''获取存储的用户名'''
    filename = 'username.json'
    if os.path.exists(filename):
        try:
            with open(filename) as f_obj:
                username = json.load(f_obj)
            return username
        except json.JSONDecodeError:
            return None
    else:
        return None

def save_username(username):
    '''保存用户名到文件'''
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

def greet_user():
    '''给用户打招呼'''
    while True:
        username = get_username()
        if username is not None:
            print('Welcome back, ' + username + '!')
        else:
            username = input('请输入用户名：')
            save_username(username)
            print('欢迎 ' + username + ' 首次到来，系统会进行登记。')
        response = input('是否继续？（是/否）：')
        if response.lower() == '否':
            break

greet_user()

import json

def get_sorted_username():
    '''如果存储了用户的名字就提取'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            return username
        
        # 如果文件不存在        
    except FileNotFoundError:
        username = input('what is your name? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you came back," + username +'!')
            
        # 如果文件存在，但是文件内容为空
    except json.JSONDecodeError:
        username = input('what is your name? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you came back," + username +'!')

def get_new_username():
    '''如果没有存储用户名，则要求用户输入'''
    filename = 'username.json'
    username = input('what is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
        
def greet_user():
    '''给用户打招呼'''
    username = get_sorted_username()
    if username:
        print('Welcome back,' + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you came back," + username +'!')

greet_user()

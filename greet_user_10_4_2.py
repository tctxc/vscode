import json

def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

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

    else:
        print('Welcome back,' + username + '!')

greet_user()
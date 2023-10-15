filename = 'guest.txt'

while True:
    user_name = input('请输入你的你昵称(输入“quit”退出)： ')
    if user_name == 'quit':
        break
    else:
        with open('guest.txt','a') as file_objct_3:
            file_objct_3.write('hello, ' + user_name.title() + '.\n')
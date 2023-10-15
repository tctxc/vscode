import json


filename = 'username.json'

username = input('What is your name? ')

with open(filename, 'a') as f_obj:
    json.dump(username,f_obj)
    print('We will remember you when you come back, '+ username.rstrip(),'!')



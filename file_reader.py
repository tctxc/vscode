filename = 'text_file\pi_million_digits.txt'


with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

#print(pi_string[:52]+'...')
#print(len(pi_string))

'''
检查一下生日是否在pi_million_digits中出现
'''
while True:
    birthday = input('Please enter your birthday by format xxxxxx (exp. 881112) :  ')
    if birthday in pi_string:
        print('Your birthday appears in the first million digits of Pi!')
    else:
        print('Your birthday DOES NOT in the first million digits of Pi!')
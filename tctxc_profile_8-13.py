def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含了解到用户的一切信息'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Asuka', 'Li', sex = 'Male', field = 'Crossdressing', wight = '75kg', hight = '177')
'''变量user_profile用于存储由build_profile函数构建出来的一个信息流（对象）'''

print(user_profile)
'''将这个信息流（对象）打印出来'''
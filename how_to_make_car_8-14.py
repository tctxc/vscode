def make_car(manufacturer, type, **kwargs):
    profile = {}
    #创建一个新的空字典，用于接收传入的位置参数值
    profile['manufacturer'] = manufacturer  # 位置参数manufacturer所获得的值存储在字典profile的键'manufacturer'上
    profile['type'] = type  # 位置参数type所获得的值存储在字典profile的键'type'上

    for key, value in kwargs.items():
        # 将以键-值对形式传入字典的值进行存储
        profile[key] = value
    return profile  #最终返回整个字典profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
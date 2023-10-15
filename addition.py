print('给我两个数字，我会进行加法运算！')
print('输入"q"可以退出程序。')

while True:
    first_number = input('\n请输入第一个数字：')
    if first_number == 'q':
        break
    second_number = input('\n请输入第二个数字：')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('请使用数字进行加法运算！')
        continue #出现异常后返回继续要求用户输入，否则answer赋值失败将引发错误

    print(answer)
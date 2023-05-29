def sandwich_making(*toppings):
    '''将客人给出的三明治配料打印出来,这个函数只有一个形参，使用了'''
    print('\n客人需要使用的配料包括： ')
    for topping in toppings:
        print('- ' + topping)

sandwich_making('pepperoni')
sandwich_making('mushrooms','green peppers','extra cheese')
sandwich_making('chicken','beaf')
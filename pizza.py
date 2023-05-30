def make_pizza(*toppings):
    '''打印出客户点的所有配料'''
    print('\nMaking pizza with the following toppings: ')
    for topping in toppings:
        print('- ' +topping)


def get_formatted_name(first,last,middle=''):
    '''
    Generate a neatly formatted full name.
    函数能够接受有姓有名，还有中间名的情况
    但是中间名作为可选的
     
    '''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


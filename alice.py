filename = 'alice.txt'

try:
    with open(filename, 'rb') as f_obj:
        contents = f_obj.read().decode('gbk', errors='replace')

except FileNotFoundError:
    msg = 'Sorry, the file '+ filename + ' does not exist.'
    print(msg)


else:
    '''
    计算文件中有多少字。
    '''
    words = contents.split()
    num_words = len(words)
    print("文件 - " + filename + "全文共计" + str(num_words) + "字。")
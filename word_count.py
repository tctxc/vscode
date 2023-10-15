def count_words(filename):
    '''
    计算文件中有多少字。
    '''
    try:
        with open(filename, 'rb') as f_obj:
            contents = f_obj.read().decode('gbk', errors='replace')

    except FileNotFoundError:
        msg = 'Sorry, the file '+ filename + ' does not exist.'
        print(msg)

    else:
        # 计算文件中出现了多少个单词the
        num_the = contents.lower().count('the')
        print("文件 - " + filename + "文中，the 出现过" + str(num_the) + "次。")


        # 计算有多少个单词
        words = contents.split()
        num_words = len(words)
        print("文件 - " + filename + "全文共计" + str(num_words) + "字。")


filenames = ['alice.txt','moby_dick.txt','little_woman','siddhartha.txt']
for filename in filenames:
    count_words(filename)
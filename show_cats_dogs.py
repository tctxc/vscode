filenames = ['cats.txt','dogs.txt','pigs.txt']



try:
    for filename in filenames:
        with open(filename, 'rb') as f_obj:
            contents = f_obj.read().decode('utf-8', errors='replace').rstrip()
            print(contents)

except FileNotFoundError:
    msg = 'Sorry, the file '+ filename + ' does not exist.'
    print(msg)

    # else:
    #     for filename in filenames:
    #         print(filename)
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')


with open(filename, 'a') as file_object_2:
    file_object_2.write('I also love finding meaning in large datasets. \n')
    file_object_2.write('I love creating apps that can turn in a brower.\n')
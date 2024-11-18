value_1, value_2 = input(), input()

with open('file_1.txt', 'w') as file_1:
    file_1.write(value_1)

with open('file_2.txt', 'w') as file_2:
    file_2.write(value_2)

with open('file_3.txt', 'w') as file_3, open('file_1.txt', 'r') as file_1, open('file_2.txt', 'r') as file_2:
    contents_1 = file_1.read()
    contents_2 = file_2.read()

    file_3.write(contents_1)
    file_3.write('\n')
    file_3.write(contents_2)

with open('file_3.txt', 'r') as file_3:
    result = file_3.read()
    print(result)
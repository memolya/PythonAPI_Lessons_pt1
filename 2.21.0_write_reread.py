file = open('file.txt', 'w')

value_1 = input()
file.write(value_1)
file.close()

content = open('file.txt', 'r')
print(content.read())
value_1, value_2 = input(), input()
fw = open('file.txt', 'w')
fw.write(value_1 + '\n' + value_2)
fw.close()

fr = open('file.txt', 'r')
print(fr.read())
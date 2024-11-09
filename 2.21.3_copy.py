value_1 = input()
fw_1 = open('file_1.txt', 'w')
fw_1.write(value_1)
fw_1.close()

fr_1 = open('file_1.txt', 'r')
content_1 = fr_1
fw_2 = open('file_2.txt', 'w')

for line in fr_1:
    # append content to second file
    fw_2.write(line)
    fw_2.close()

fr_2 = open('file_2.txt', 'r')
print(fr_2.read())
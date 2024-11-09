films = input().split()
fw = open('file.txt', 'w')

for film in films:
        fw.write(film + '\n')
fw.close()

fr = open('file.txt', 'r')
content = (fr.read())
content_lst = content.split()
fr.close()

for line in content_lst[0:-1]:
    print(line + '\n' + '*'*5)
print(content_lst[-1])
films = input().split()
fw = open('file.txt', 'w')

for film in films:
        fw.write(film + '\n')
fw.close()

fr = open('file.txt', 'r')

counter = 0
for i in fr:
    counter += 1

print(counter)
fr.close()
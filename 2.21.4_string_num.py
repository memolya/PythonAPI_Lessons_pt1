films = input().split()
value_1 = input()

fw = open('file.txt', 'w')
for film in films:
    fw.write(film + '\n')
fw.close()

fr = open('file.txt', 'r')
films_lst = list(fr)

for count, item in enumerate(films_lst, start=1):
    if value_1 in item:
        print(count)

fr.close()
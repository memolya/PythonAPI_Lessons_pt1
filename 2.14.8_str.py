films = input().split()
total = 0

for film in films:
    if film.isalpha(): #если текст
        total += len(film)
        continue
    else:
        film_num = int(film) #если число
        total += film_num
        continue

print(total)
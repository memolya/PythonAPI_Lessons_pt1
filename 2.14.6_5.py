films = input().split()
for film in films:
    if len(film) > 5:
        print(film)
        continue
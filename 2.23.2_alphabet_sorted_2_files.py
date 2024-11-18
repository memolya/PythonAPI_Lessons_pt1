films = input().split()

with open('file_1.txt', 'w') as file_1:
    for film in films:
        file_1.write(str(film))
        file_1.write('\n')

with open('file_1.txt', 'r') as file_1:
    movies = []
    for film in films:
        movies.append(film)

with open('file_2.txt', 'w') as file_2:
    movies.sort()
    for movie in movies:
        file_2.write(str(movie))
        file_2.write('\n')

with open('file_2.txt', 'r') as file_2:
    contents = file_2.read()
    print(contents)
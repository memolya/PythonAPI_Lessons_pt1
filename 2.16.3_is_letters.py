films = input().split()
for name in films:
    if name.isalpha():
        print(name)
    else:
        break

# films = input().split()
# i = 0
# while films[i].isalpha():
#     print(films[i])
#     i += 1
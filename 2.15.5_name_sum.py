films = input().split()
sum = 0
for name in films:
    sum += len(name)
print(sum)
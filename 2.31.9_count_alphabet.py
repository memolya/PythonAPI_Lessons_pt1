letter = input().split()
counter = 0

for index, word in enumerate(letter, start = 1):
    counter += index

print(counter)
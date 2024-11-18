numbers = list(map(int, input().split()))

with open('file.txt', 'w') as file:
    for number in numbers:
        file.write(str(number))
        file.write('\n')

with open('file.txt', 'r') as file:
    all = []
    for number in numbers:
        all.append(int(number))
    print(sum(all))



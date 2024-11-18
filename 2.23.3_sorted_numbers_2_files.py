numbers = list(map(int, input().split()))

with open('file_1.txt', 'w') as file_1:
    for number in numbers:
        file_1.write(str(number))
        file_1.write('\n')

with open('file_1.txt', 'r') as file_1:
    num = []
    for number in numbers:
        num.append(int(number))

with open('file_2.txt', 'w') as file_2:
    num.sort(reverse=True)
    for number in num:
        file_2.write(str(number))
        file_2.write('\n')

with open('file_2.txt', 'r') as file_2:
    contents = file_2.read()
    print(contents)
numbers = list(map(int, input().split()))

with open('file_1.txt', 'w') as file_1:
    for number in numbers:
        file_1.write(str(number))
        file_1.write('\n')

with open('file_1.txt', 'r') as file_1:
    unevens = []
    for i in range(len(numbers)+1): #range to use i as index and numbers[i] as contents
        if i % 2 == 0:
            unevens.append(numbers[i])

with open('file_2.txt', 'w') as file_2:
    for number in unevens:
        file_2.write(str(number))
        file_2.write('\n')

with open('file_2.txt', 'r') as file_2:
    contents = file_2.read()
    print(contents)
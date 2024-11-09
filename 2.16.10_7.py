numbers = list(map(int, input().split()))
counter = 0

for number in numbers:
    while number > 7:
        print(number)
        break
    else:
        break
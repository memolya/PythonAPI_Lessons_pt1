numbers = list(map(int, input().split()))
for number in numbers:
    if number < 0:
        print(number)
        break
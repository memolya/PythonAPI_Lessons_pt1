numbers = list(map(int, input().split()))
for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
        print(number)
        continue
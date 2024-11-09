numbers = list(map(int, input().split()))
summed = 0
for number in numbers:
    if number > 0:
        summed += number
        continue
    else:
        continue
print(summed)
numbers = list(map(int, input().split()))
positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
        continue
    else:
        negative += 1
        continue

print(positive, negative, sep = '\n')
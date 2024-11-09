a, b = int(input()), int(input())

greater = max(a,b)
smaller = min(a,b)
summed = 0

while smaller <= greater:
    summed += smaller
    smaller += 1

print(summed)
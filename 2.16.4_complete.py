a = int(input())
n = 1
counter = 0

while counter != a:
    if a % n == 0:
        print(n)
        n += 1
        counter += 1
    else:
        counter += 1
        n += 1
        continue

a, b = input(), input()
counter = 0
for symbol in a:
    if b in symbol:
        counter += 1
print(counter)
a = input()
counter = 0
for symbol in a:
    if 'a' in symbol or 'b' in symbol or 'i' in symbol:
        counter += 1
print(counter)
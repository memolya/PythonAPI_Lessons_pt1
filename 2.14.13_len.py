text = input()
counter_special_symbols = 0

for sybmol in text:
    if not sybmol.isalpha() and not sybmol.isdigit():
        counter_special_symbols += 1

print(counter_special_symbols)

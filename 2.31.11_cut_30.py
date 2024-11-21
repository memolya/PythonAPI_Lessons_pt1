sentence = input()
first_30 = sentence[:31]
remnants = ''

for i in sentence[31:]:
    if i != ' ':
        remnants += i
    else:
        break

print(first_30, remnants, '!', sep = '')
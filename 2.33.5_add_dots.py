var = input()
new_str = ''

for i in var:
    if i == '.':
        new_i = i.replace('.', '..')
        new_str += new_i
    else:
        new_str += i

print(new_str)

# print(input().replace('.', '..'))
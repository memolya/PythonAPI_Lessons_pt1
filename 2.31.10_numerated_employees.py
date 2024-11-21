new_list = input().split()
list_starts_w_digit = []

for name in new_list:
    if name[0].isdigit():
        list_starts_w_digit.append(name)

for name in list_starts_w_digit:
    if name[1] == ')' or name[1] == '.':
        print(name)
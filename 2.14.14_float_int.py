new_list = input().split()
counter = 0

for i in new_list:
    if i.isdigit():
        counter += 1
    else:
        try: #try for float as isdigit doesn't include floats
            x = float(i)
            counter += 1
        except ValueError:
            continue

print(counter)

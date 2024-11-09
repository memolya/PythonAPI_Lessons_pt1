# new_list = input().split()
# index = 1
#
# for word in new_list:
#     print(index, '.', word, sep = '')
#     index += 1

list = input().split()
for index, name in enumerate(list, 1): #list to iterate and 1 as a starting point of index
    print(f'{index}.{name}')
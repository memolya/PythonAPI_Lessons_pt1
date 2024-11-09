dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict_result = dict1 | dict2 #replace b with the value from the 2nd dictionary

for key, value in dict_result.items():
    print(f'{key} - {value}')


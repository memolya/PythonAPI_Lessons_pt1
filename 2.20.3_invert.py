dict1 = {'a': 1, 'b': 2, 'c': 3}
inv_map = {v: k for k, v in dict1.items()}

for key, value in inv_map.items():
    print(f'{key} - {value}')
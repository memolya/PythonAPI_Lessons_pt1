data = {'a': 1, 'b': 2, 'c': 3}
dl = input()

try:
    del data[dl]
    for key, value in data.items():
        print(f'{key} - {value}')

except KeyError:
    for key, value in data.items():
        print(f'{key} - {value}')

# [print(f'{key} - {value}') for key, value in data.items()]
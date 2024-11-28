key = int(input())

keys = list(range(1, key+1))
values = []

for i in keys:
    i = i**2
    values.append(i)

for key, value in zip(keys, values):
    print(f'{key} - {value}')
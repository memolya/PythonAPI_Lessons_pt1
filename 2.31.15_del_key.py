data = {'a': 1, 'b': 0, 'c': 3, 'd': 0}
new_dict = {}

for key, value in list(data.items()): #RuntimeError: dictionary changed size during iteration
                                      #In Python 3, you need list(d.items()) as mentioned in @jared's answer.
    if value == 0:
        del data[key]
    else:
        print(f'{key} - {value}')

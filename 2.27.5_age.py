def new_func(name, by):
    age = 2024 - by
    result = f'Меня зовут {name}, мне {age}.'
    return result

print(new_func(name=input(), by=int(input())))
var = input()
new_var = ''
count = 0  # Счётчик для номера вхождения

for char in var:
    if char == '#':
        count += 1  # Увеличиваем счётчик для каждого символа '#'
        new_var += str(count)  # Заменяем '#' на номер вхождения
    else:
        new_var += char  # Оставляем символ без изменений
        count += 1

print(new_var)

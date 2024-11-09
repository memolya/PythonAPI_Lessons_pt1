new_dict = {'Имя': 'Светлана', 'Пароль': 'qwer1234', 'Код': 1984}
# 1)Имя - скрываются все символы, кроме первой буквы.
# 2)Пароль - скрываются все символы
# 3)Код восстановления - скрываются все символы, кроме последней цифры.

for key, value in new_dict.items():
    if key == 'Имя':
        print(value[0], '#' * (len(value)-1), sep = '')
    elif key == 'Пароль':
         print('#' * (len(value)), sep = '')
    else:
        new_value = str(value)
        print('#' * (len(new_value)-1), new_value[-1], sep = '')
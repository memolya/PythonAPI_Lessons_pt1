number = input()

#country
if number[0] == '+':
    country = '+7'
    updated_string = number[2:]
else:
    country = '+7'
    updated_string = number[1:]

#operator
operator = updated_string[0:3]
#6 digits
six_digits = updated_string[3:6]
#2 digits - a
two_didits_a = updated_string[6:8]
#2 digits - b
two_didits_b = updated_string[8:10]

print(f'{country} ({operator}) {six_digits}-{two_didits_a}-{two_didits_b}')

# s = [x for x in input() if x.isdigit()]   #Генератор списка [x for x in input() if x.isdigit()] фильтрует только цифры из введённой строки.
                                            #Метод isdigit() проверяет, является ли символ цифрой. Только цифры добавляются в список s.

# result = '+7 (XXX) XXX-XX-XX'
# for digit in s[1:]:                        #Берём все цифры из списка s, начиная со второго элемента (s[1:]), так как первый элемент уже учтён в префиксе +7.
#     result = result.replace('X', digit, 1) #Метод replace('X', digit, 1) заменяет только первое вхождение символа X в строке на текущую цифру.
#
# print(result)
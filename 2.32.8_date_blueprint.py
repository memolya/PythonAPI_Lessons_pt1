text = input()

sep = '.'

#ищем день
first_sep_index = text.find(sep)
day = text[:first_sep_index]

#если день из 1 цифры - добавляем 0 в начале
if len(day) < 2:
    day = '0'+day

#ищем месяц
text_without_day = text[first_sep_index+1:] #убираем точку перед месяцем
second_sep_index = text_without_day.find(sep)
month = text_without_day[:second_sep_index]
if len(month) < 2:
    month = '0'+month

year = text[-4:len(text)+1]

print(f'{day}.{month}.{year}')

# s = input().split('.')
# for i in range(len(s)):
#     if len(s[i]) < 2:
#         s[i] = '0'+ s[i]
# print(*s, sep = '.')


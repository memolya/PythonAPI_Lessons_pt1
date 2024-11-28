mail_data = {'address': 'test@test.ru', 'subject': 'Спец.письмо', 'text': 'Царский указ'}
address, subject, text = "", "", "" #инициализация вне блока try-except для большей читаемости

try:
    address, subject, text = input(), input(), input()
except EOFError:
    address, subject, text = "", "", "" #Ошибка ввода! Используем значения по умолчанию
                                        #Если ошибка не возникает, но переменные определены только внутри блока try, они недоступны за его пределами.

def check_mail(address, subject, text):

    #mail_data['address']: - Квадратные скобки (['key']) используются для обращения к значению по указанному ключу в словаре mail_data.
    #Здесь 'address' — это ключ в словаре mail_data.
    #Код возвращает значение, связанное с этим ключом, то есть строку 'test@test.ru' (в примере словаря).

    #Значение из словаря mail_data['address'] (в данном случае 'test@test.ru') сравнивается с пользовательским вводом, сохранённым в переменной address.
    #Аналогично, mail_data['subject'] извлекает значение по ключу 'subject' ('Спец.письмо' в данном словаре) и сравнивается с переменной subject.
    if address and subject and address == mail_data['address'] and subject == mail_data['subject'] and (text == mail_data['text'] or not text):
        return 'Good'
    else:
        return 'Bad'

print(check_mail(address, subject, text))

#
# mail_data = {'address': 'test@test.ru', 'subject': 'Спец.письмо', 'text': 'Царский указ'}
#
# def safe_input(prompt=''):
#     try:
#         return input(prompt).strip()
#     except EOFError:
#         return ''
#
#
# use1 = input()
# use2 = input()
# use3 = safe_input()
#
# if use1 == mail_data['address'] and use2 == mail_data['subject'] and (use3 == mail_data['text'] or not use3):
#     print("Good")
# else:
#     print("Bad")
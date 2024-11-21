mail_data = {'address': 'test@test.ru', 'subject': 'Спец.письмо', 'text': 'Царский указ'}

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
    if mail_data['address'] == address and mail_data['subject'] == subject:
        return 'Good'
    else:
        return 'Bad'

print(check_mail(address, subject, text))
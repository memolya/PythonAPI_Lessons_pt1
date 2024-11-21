# url = input().split()
# new_list = []
#
# for inst in url:
#     try:
#         www, name, domain = map(str, inst.split('.'))
#         new = name + '.' + domain
#         new_list.append(new)
#     except ValueError:
#         www, name, domain, query = map(str, inst.split('.'))
#         new = name + '.' + domain
#         new_list.append(new)
# print(new_list)
#
# for name in new_list:
#     try:
#         name, other, query = map(str, name.split('/'))
#         print(name)
#     except ValueError:
#         print(name)
#         #этот кусок не отрабатывает для обоих тестов, потому что разбивка по / учитывает либо 1 слеш в ссылке (если у нас только параметры
#         # name, other. Или же добавляем параметр query для ссылок с двумя слешами, но это сломает обработку ссылок
#         #с одним слешом
#

from urllib.parse import urlparse

# Ввод списка URL-адресов
url = input().split()

# Обработка каждого URL-адреса
for inst in url:
    try:
        parsed_url = urlparse(inst)  # Разбираем URL-адрес
        # Извлекаем имя сайта (без 'www.', если оно есть)
        domain = parsed_url.netloc.replace("www.", "")
        print(domain)
    except Exception as e:
        print(f"Ошибка обработки URL: {inst}, {e}")

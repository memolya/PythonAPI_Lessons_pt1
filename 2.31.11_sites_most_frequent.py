url = input().split()
domain_count = {}

# Обработка каждого URL-адреса
for inst in url:
    try:
        # Удаляем протокол (http:// или https://) и всё после слеша
        if "://" in inst:
            inst = inst.split("://")[1]                        #Метод .split("://") делит строку inst на две части, используя :// в качестве разделителя.
                                                               #Индекс [1] извлекает второй элемент списка (часть после ://), чтобы оставить только домен и путь, игнорируя протокол.
                                                               #["https", "example.com/path"] - inst = "example.com/path" ([1] для inst.split)
                                                               #Если [1] не указать, метод .split("://") вернёт весь список: ["https", "example.com/path"]


        domain = inst.split("/")[0]                            # Извлекаем домен (до первого слеша)
        # Удаляем 'www.' из домена, если оно есть
        domain = domain.replace("www.", "")
        domain_count[domain] = domain_count.get(domain, 0) + 1 #Если домен уже есть в словаре domain_count, его счётчик увеличивается на 1.
                                                               #Если домен отсутствует, он добавляется со значением 1.
        most_domain = max(domain_count, key=domain_count.get)  #Функция max находит ключ (домен) с максимальным значением
                                                               # (количеством вхождений) в словаре domain_count.
    except Exception as e:
        print(f"Ошибка обработки URL: {inst}, {e}")

print(most_domain)
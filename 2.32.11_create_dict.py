movie_info = ("Название 'Армагеддон', Год выпуска '1998', "
              "Продолжительность '144', Жанр 'Фантастика', Режиссер 'Майкл Бэй', В главных ролях 'Брюс Уиллис', Статус фильма 'Брюса жалко'")

# Разбиваем строку на пары key-value
pairs = [x.strip() for x in movie_info.split(",")]


movie_dict = {}
for pair in pairs:
    key, value = pair.split(" '", 1)  # Разделяем ключ и значение
    movie_dict[key.strip()] = value.strip("'")  # Очищаем от пробелов и одиночных кавычек

# Выводим словарь
for key, value in movie_dict.items():
    print(f'{key} : {value}')
import os

# Ввод пути к файлу
file_path = input()

# Извлечение пути без имени файла
directory_path = os.path.dirname(file_path)

# Определяем тип слэша в исходном пути
if "\\\\" in file_path:  # Проверяем наличие двойных обратных слэшей
    sep = "\\\\"
elif "\\" in file_path:  # Проверяем одинарные обратные слэши
    sep = "\\"
else:  # Используем прямой слэш (Linux/macOS)
    sep = "/"

# Добавляем завершающий слэш, если его нет
if not directory_path.endswith(sep):
    directory_path += sep

# Вывод результата
print(directory_path)


# без библиотеки os
# Ввод пути к файлу
file_path = input()

# Определяем разделитель (слэш или обратный слэш)
if "\\\\" in file_path:  # Проверяем двойные обратные слэши
    sep = "\\\\"
elif "\\" in file_path:  # Проверяем одинарные обратные слэши
    sep = "\\"
else:  # Используем прямой слэш (Linux/macOS)
    sep = "/"

# Удаляем имя файла, оставляя только путь
# Находим последний разделитель
last_sep_index = file_path.rfind(sep)
if last_sep_index != -1:
    #Срез строки до последнего разделителя оставляет только путь, исключая имя файла.
    #Добавляем len(sep) к индексу, чтобы включить завершающий слэш в результат.
    directory_path = file_path[:last_sep_index + len(sep)]
else:
    directory_path = file_path  # Если разделитель не найден, возвращаем исходный путь

# Вывод результата
print(directory_path)


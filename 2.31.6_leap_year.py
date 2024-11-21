def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Ввод списка строк
new_list = input().split()

# Вывод дат, относящихся к високосным годам
for date in new_list:
    try:
        day, month, year = map(int, date.split("."))  # Разбиваем дату на день, месяц и год
        if is_leap_year(year):
            print(date)
    except ValueError:
        print(f"Некорректный формат даты: {date}")

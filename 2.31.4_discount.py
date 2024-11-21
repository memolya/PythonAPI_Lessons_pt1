a = int(input())

# Стоимость пакета молока без скидки
price = 100

# Расчет для каждой акции
# 1 пакет молока (без скидки)
packages_1 = a // price

# 2 пакета молока (скидка 30%)
price_2 = 2 * price * 0.7
packages_2 = (a // price_2) * 2

# 3 пакета молока (скидка 40%)
price_3 = 3 * price * 0.6
packages_3 = (a // price_3) * 3

# 5 пакетов молока (скидка 50%)
price_5 = 5 * price * 0.5
packages_5 = (a // price_5) * 5

# Вывод результатов
print(packages_1, int(packages_2), int(packages_3), int(packages_5), sep = '\n')
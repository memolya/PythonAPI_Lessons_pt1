numbers = list(map(int, input().split()))
print(sum(numbers))

# 3. 'map(int, ...)': Функция map применяет функцию 'int' к каждому элементу списка, полученного на предыдущем шаге. 'int' преобразует строку в целое число. Т.е. map(int, ['10', '20', '30']) вернет объект-итератор, который по очереди выдаст числа 10, 20 и 30. Важно понимать, что map не создает новый список сразу, а именно возвращает объект-итератор, или "ленивый" объект, который создается "на лету". Нам такой объект не подходит, поэтому переходим к следующему шагу:
# 4. 'list(...)': Функция list преобразует объект-итератор, возвращенный функцией map, в список. Т.е. list(map(int, ['10', '20', '30'])) вернет список целых чисел [10, 20, 30].

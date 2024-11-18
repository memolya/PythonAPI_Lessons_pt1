var_1, var_2 = int(input()), int(input())
my_list = [0, 2, 4]
try:
    result = int(my_list[var_1] / my_list[var_2])
    print('Good')
except ZeroDivisionError:
    print('Деление на ноль недопустимо')
except IndexError:
    print('Индекс вне диапазона')
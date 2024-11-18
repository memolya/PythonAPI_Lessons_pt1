index = int(input())
my_list = [10, 20, 30, 40, 50]

try:
    print(my_list[index])
except IndexError:
    print('Индекс вне диапазона')
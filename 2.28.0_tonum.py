line = input()
try:
    result = int(line)
    print(result)
except ValueError:
    result = 'Невозможно преобразовать строку в целое число'
    print(result)

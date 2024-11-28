data = {'a': 10, 'b': 20, 'c': 15}

# list out keys and values separately
key_list = list(data.keys())
val_list = list(data.values())

# print key with val 20
#Вычисляет максимальное значение среди значений словаря: max([10, 20, 15]) = 20.
#Находит индекс этого значения (20) в списке val_list: индекс 1.
position = val_list.index(max(data.values()))
#Использует индекс 1 (из переменной position) для извлечения ключа из key_list: key_list[1] = 'b'.
print(f'{key_list[position]} - {max(val_list)}')
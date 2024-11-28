numbers = list(map(int, input().split()))

new_dict = {}

for num in numbers:
    counter = numbers.count(num)
    new_dict[num] = counter     #В Python словари используют ключи, которые должны быть уникальными. Если в словарь добавить новую пару ключ-значение с ключом, который уже существует, старое значение будет перезаписано.
                                #Таким образом, словарь автоматически исключает дублирующиеся ключи.
                                #new_dict[num] = counter: Добавляет элемент num в словарь new_dict как ключ, а его частоту — как значение.
sorted_dict = sorted(new_dict.items())
# print(type(sorted_dict)) #class list

for key, value in dict(sorted_dict).items(): #add dict to return to dict type
    print(f'{key} - {value}')


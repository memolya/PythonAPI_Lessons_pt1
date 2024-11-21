def is_name_in_list(new_list, name):
    name = name.casefold() # Сравниваем строки без учёта регистра
    for i in new_list:
        if name in i.casefold(): # Сравниваем строки без учёта регистра
            return 'Good' # Если нашли, сразу возвращаем "Good"
    return 'Bad'          # Если цикл завершился, значит, имя не найдено

print(is_name_in_list(new_list=input().split(), name=input()))
path = input()

# Определяем разделитель (слэш или обратный слэш)
if '\\\\' in path:
    sep = '\\\\'
    last_sep_index = path.rfind(sep) #находит самое последнее вхождение разделителя и использует его как границу для извлечения пути
    file_name = path[last_sep_index + 2:]

elif '\\' in path:
    sep = '\\'
    last_sep_index = path.rfind(sep)
    file_name = path[last_sep_index + 1:]

else:
    sep = '/'
    last_sep_index = path.rfind(sep)
    file_name = path[last_sep_index + 1:]

if '.' in file_name:
    sep = '.'
    last_sep_index = file_name.rfind(sep)
    file_name_final = file_name[:last_sep_index]
    
print(file_name_final)
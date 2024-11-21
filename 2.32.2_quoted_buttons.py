text = input()
buttons = ["Согласен", "Логин", "Войти"]
for i in buttons:
    text = text.replace(i, f'"{i}"')        #Метод .replace() обрабатывает текст как строку целиком.
                                            # Работает с любым количеством кнопок, даже если кнопки идут подряд или разделены символами.
                                            #Вся строка редактируется за одну итерацию.
print(text)


# text = input().split()
#
# quoted_words = []
#
# for word in text:
#     if word.casefold() in ["войти", "согласен", "логин"]:  # Условие для выбора слов
#         quoted_words.append(f'"{word}"')
#     else:
#         quoted_words.append(word)
#
# quoted_sentence = " ".join(quoted_words) #метод .join() объединяет все элементы списка quoted_words в одну строку, используя пробел (" ") как разделитель.
# print(quoted_sentence)

#Добавьте обработку пунктуации, чтобы корректно обрабатывать слова с символами, а также сохранение пунктуации:
# import string
#
# text = input().split()
#
# quoted_words = []
#
# for word in text:
#     # Отделяем пунктуацию от слова
#     stripped_word = word.strip(string.punctuation).casefold()
#     if stripped_word in ["войти", "согласен", "логин"]:
#         # Сохраняем пунктуацию
#         quoted_words.append(f'"{word.strip(string.punctuation)}"{word[len(word.strip(string.punctuation)):]}')
#     else:
#         quoted_words.append(word)
#
# quoted_sentence = " ".join(quoted_words)
# print(quoted_sentence)
#
# Логика исправленного кода:
# string.punctuation:
# Используется для удаления знаков пунктуации вокруг слова.
# word.strip(string.punctuation):
# Убирает пунктуацию для проверки кнопок.
# Восстановление пунктуации:
# После оборачивания в кавычки возвращаются знаки пунктуации.
# Итог:
# Первый код более универсален и работает корректно благодаря использованию .replace().
# Второй код требует дополнительной обработки пунктуации и проверки условий, чтобы избежать ошибок.


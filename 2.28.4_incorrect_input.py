def element_exists(lst, element):
    try:
        lst.index(element)
        result = element
        return result

    except ValueError:
        result = 'Некорректный ввод'
        return result


list_1 = list(range(1, 4))
print(element_exists(list_1, element=int(input())))

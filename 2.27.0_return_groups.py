def new_func(num):
    if num > 6:
        result = 'Bad'
    elif 3 >= num >= 1:
        if num == 2:
            result = 'Два'
        else:
            result = 'Bad'
    elif 6 >= num >= 4:
        if num == 5:
            result = 'Пять'
        else:
            result = 'Bad'
    else:
        result = 'Bad'

    return result

print(new_func(num=int(input())))
def new_func(num):
    if num % 7 == 0:
        result = 'Good'
    else:
        result = 'Bad'

    return result

print(new_func(num=int(input())))
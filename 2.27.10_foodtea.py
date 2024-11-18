def new_func(food, tea):
    if tea > food:
        result = 'Bad'
        return result
    else:
        result = tea*500 + food*3000
        return result

print(new_func(food=int(input()), tea=int(input())))
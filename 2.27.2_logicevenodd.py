def even():
    result = 'ЧЕТ'
    return result

def odd():
    result = 'НЕЧЕТ'
    return result

def logic(num):
    if num % 2 == 0:
        return even()
    else:
        return odd()

print(logic(num=int(input())))
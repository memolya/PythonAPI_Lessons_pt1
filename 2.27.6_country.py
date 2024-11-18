def russia(name):
    result = f'Здравствуй {name}'
    return result

def england(name):
    result = (f'Hello {name}')
    return result

def logic(name, country):
    if country == 'Россия':
        return russia(name)
    else:
        return england(name)

print(logic(name=input(), country=input()))



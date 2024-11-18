def new_func(name):
    second_name = name[0]
    acronym = name[1][0] + '.' + name[2][0] + '.'
    result = second_name + ' ' + acronym
    return result

print(*{new_func(name=input().split())})


# def new_function(full_name: str) -> None:
#     last_name, first_name, patronymic = full_name.split()
#     print(f'{last_name} {first_name[0]}.{patronymic[0]}.')
#
#
# new_function(input())
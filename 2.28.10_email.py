def new_func(email):
    compulsory = ['@mail.ru', '@rambler.ru', '@.ru']
    for i in compulsory:
        if i in email:
            flag = True
            break
        else:
            flag = False
            continue
            print('Bad')

    if flag == True:
        print('Good')
    else:
        print('Bad')

new_func(email=input())


# def new_function(email: str) -> None:
#     is_valid = True
#     if '@' not in email:
#         is_valid = False
#     else:
#         if not email.endswith('.ru'):
#             is_valid = False
#
#     if is_valid:
#         print('Good')
#     else:
#         print('Bad')
#
#
# new_function(input())
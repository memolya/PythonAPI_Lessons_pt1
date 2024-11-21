person_data= {'Login': 'User1', 'Password': 'Qwer_1234'}
login, password = input(), input()

def check_creds():
    if login in person_data.values() and password in person_data.values():
        return 'Good'
    else:
        return 'Bad'

print(check_creds())
inn = input()
def inn_check(inn):
    if len(inn) == 10 or len(inn) == 12:
        return 'Good'
    return 'Bad'


print(inn_check(inn))

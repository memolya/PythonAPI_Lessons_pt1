def new_func(day, balance):
    if day > 3 or day < 1:
        # if days not in range(1, 4):
        return('Bad')
    elif balance < 30:
        return('Bad')
    else:
        days = range(1, day+1)
        balance_counter = balance - 7

        with open('file.txt', 'w') as file:
            for i in days:
                file.write(f'{i} день - баланс {balance} - списалось 7 - осталось {balance_counter}')
                balance -= 7
                balance_counter -= 7
                file.write('\n')

    with open('file.txt', 'r') as file:
        contents = file.read()
        return contents

print(new_func(day=int(input()), balance=int(input())))
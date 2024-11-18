def new_func(balance, transaction):
    if balance > transaction:
        result = balance - transaction
        return result
    elif transaction > balance:
        result = 'Не хватает денежных средств'
        return result
    else:
        result = 0
        return result

print(new_func(balance=int(input()), transaction=int(input())))
def discount(var):
    if var < 10000:
        disc = 0
        price = var
        print(price, disc, sep = '\n')
    else:
        disc = var*0.3
        price = var - disc
        print(int(price), int(disc), sep = '\n')

discount(var=int(input()))


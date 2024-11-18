def new_function(number):
    rng = []
    counter = 2
    flag = True

    while counter < number:
        rng.append(counter)
        counter += 1

    for divider in rng:
        num = number
        if num == 2:
            flag = True
            break
        elif num % divider == 0:
            flag = False
            break
        else:
            flag = True
            continue

    if flag == True:
        print('Good')
    else:
        print('Bad')

new_function(number=int(input()))
var = input()
minutes = int(input())
def count_time():
    # var_hour, var_minutes = var.split(':')[0], var.split(':')[1]
    var_hour, var_minutes = map(int, var.split(':'))

    #Если минуты во времени + добавочные < 60
    minutes_combined = int(var_minutes) + minutes

    if minutes_combined <= 59:
        print(f'{var_hour}:{minutes_combined}')

    #Если минуты во времени + добавочные > 60
    else:
        hour_new = int(var_hour) + 1
        minute_new = abs(60 - minutes_combined) #модуль числа

        #если часы + добавочные <= 23
        if hour_new <= 23:
            #минуты в остатке 2 или 1-значные
            if minute_new >= 10:
                print(f'{hour_new}:{minute_new}')
            else:
                print(f'{hour_new}:0{minute_new}')

        #если часы + добавочные > 23
        elif hour_new > 23:
            #минуты в остатке 2 или 1-значные
            if minute_new >= 10:
                print(f'00:{minute_new}')
            else:
                print(f'00:0{minute_new}')


if minutes > 60:
    print('Bad')
else:
    count_time()


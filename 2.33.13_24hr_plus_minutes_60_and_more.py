var = input()
minutes = int(input())
def count_time():
    # var_hour, var_minutes = var.split(':')[0], var.split(':')[1]
    var_hour, var_minutes = map(int, var.split(':'))

    #Если минуты во времени + добавочные < 60
    minutes_combined = int(var_minutes) + minutes

    if minutes_combined <= 59:
        return f'{var_hour}:{minutes_combined}'

    #Если минуты во времени + добавочные > 60
    else:
        hour_new = int(var_hour) + 1
        minute_new = abs(60 - minutes_combined) #модуль числа

        #если часы + добавочные <= 23
        if hour_new <= 23:
            #минуты в остатке 2 или 1-значные
            if minute_new >= 10:
                return f'{hour_new}:{minute_new}'
            else:
                return f'{hour_new}:0{minute_new}'

        #если часы + добавочные > 23
        elif hour_new > 23:
            #минуты в остатке 2 или 1-значные
            if minute_new >= 10:
                return f'00:{minute_new}'
            else:
                return f'00:0{minute_new}'

result = count_time()

def minutes_input_bigger_sixty(result):
    result_h, result_m = map(int, result.split(':'))
    if result_m > 59:
        hours_to_add = result_m // 60
        hours_2 = result_h + hours_to_add
        minutes_2 = result_m - (60*hours_to_add) #вычитаем из минут > 59 то, что уже прибавили к часам
        #часы <= 23
        # минуты и часы двузначные
        if 10 <= hours_2 <= 23 and 10 <= minutes_2 <= 59:
            return f'{hours_2}:{minutes_2}'
        #минуты однозначные, часы двузначные
        elif 10 <= hours_2 <= 23 and minutes_2 <= 9:
            return f'{hours_2}:0{minutes_2}'
        #минуты однозначные, часы однозначные
        elif 1 <= hours_2 <= 9 and minutes_2 <= 9:
            return f'0{hours_2}:0{minutes_2}'
        #минуты двузначные, часы однозначные
        elif 1 <= hours_2 <= 9 and 10 <= minutes_2 <= 59:
            return f'0{hours_2}:{minutes_2}'

        #часы >23
        else:
            # минуты в остатке 2 или 1-значные
            if minutes_2 >= 10:
                return f'00:{minutes_2}'
            else:
                return f'00:0{minutes_2}'

minutes_input_bigger_sixty(result)

#печать результата
result_h, result_m = map(int, result.split(':'))
if result_m <= 59:
    print(result)
else:
    print(minutes_input_bigger_sixty(result))





var = input()

var_hour, var_minutes = var.split(':')[0], var.split(':')[1]

if 0 <= int(var_hour) <= 11:
    print(f'am - {var}')

elif 12 <= int(var_hour) <= 23:
    var_hour_new = int(var_hour) - 12
    print(f'pm - {var_hour_new}:{var_minutes}')
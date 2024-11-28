var = int(input())
var_nums = list(range(1, var+1))

for i in var_nums:
    if var == i**3:
        flag = True
        break
    else:
        flag = False

if flag == True:
    print('Good')
else:
    print('Bad')



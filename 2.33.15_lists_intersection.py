var_1, var_2 = list(input()), list(input())

if list(set(var_1) & set(var_2)): #если есть пересечения
    print('Good')
else:
    print('Bad')
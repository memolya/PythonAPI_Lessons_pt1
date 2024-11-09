numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

united = numbers_1 & numbers_2 & numbers_3
if bool(united) is True:
    print('Good')
else:
    print('Bad')
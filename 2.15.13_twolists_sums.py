numbers_1, numbers_2 = list(map(int, input().split())), list(map(int, input().split()))
sum_1 = sum(numbers_1)
sum_2 = sum(numbers_2)
if sum_1 > sum_2:
    print('1')
else:
    print('2')

# numbers1 = list(map(int, input().split()))
# numbers2 = list(map(int, input().split()))
#
# print(1 if sum(numbers1) > sum(numbers2) else 2)
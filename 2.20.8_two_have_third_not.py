numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

united_1_2 = numbers_1 & numbers_2
absent_in_third = united_1_2 - numbers_3
print(*absent_in_third)
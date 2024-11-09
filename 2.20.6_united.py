numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))

united = list(numbers_1 | numbers_2) #unite the set to get uniques, list it to sort
print(*sorted(united), sep = '\n')
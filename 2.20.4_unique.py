# numbers = set(map(int, input().split()))
# print(*numbers, sep = '\n') #sorted by set logic

numbers = list(map(int, input().split()))
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(*result, sep='\n')
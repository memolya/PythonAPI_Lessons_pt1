numbers = list(map(int, input().split()))
for num in numbers[::2]:
    print(num)

# numbers = list(map(int, input().split()))
# for x in numbers:
#   if x in numbers[::2]:
#     print(x)

# numbers = list(map(int, input().split()))
# print(*[number for i, number in enumerate(numbers) if i % 2 == 0], sep='\n')
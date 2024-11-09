numbers = list(map(int, input().split()))
evens_sum = 0
for num in numbers:
    if num % 2 == 0:
        evens_sum += num
print(evens_sum)
numbers = list(map(int, input().split()))

for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
        print(numbers[i+1])
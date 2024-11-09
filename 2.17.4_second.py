numbers = list(map(int, input().split()))
biggest = max(numbers)
new_list = []

for number in numbers:
    if number == biggest:
        continue
    else:
        new_list.append(number)

print(max(new_list))

# numbers = list(map(int, input().split()))
#
# numbers.sort(reverse=True)
# print(numbers[1])
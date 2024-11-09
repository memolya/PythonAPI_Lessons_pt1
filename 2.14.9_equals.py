from itertools import count

numbers = list(map(int, input().split()))
counter_pairs = 0

for num in numbers:
    number_counted = numbers.count(num)
    if number_counted == 2:
        counter_pairs += 1
        numbers.remove(num) #remove the 1st element from a pair already counted
        continue

print(counter_pairs)

amount, minimum = int(input()), int(input())
counter_days = 0
starting_point = amount

while amount > minimum:
    counter_days += 1
    amount = amount - (starting_point * 0.1)
print(counter_days)
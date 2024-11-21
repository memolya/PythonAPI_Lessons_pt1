initial_cost = int(input())
days = list(range(1,11))
result = []

for day in range(1, len(days)+1):
    result.append(initial_cost)
    cost = initial_cost - initial_cost*0.01
    initial_cost = cost

print(int(result[-1]))
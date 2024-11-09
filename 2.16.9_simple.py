numbers = list(map(int, input().split()))
list_simples = []

for number in numbers:
    for divider in range(2, number):
        if number % divider != 0:
            state = True
        else:
            state = False
            break

    if state == True:
        list_simples.append(number)

print(*list_simples, sep='\n')
numbers = list(range(1, 11))
import math

holder = 0 #using holder to move to the next element in cycle
for i in numbers:
    sq_1 = (numbers[holder])**2
    # print('sq_1 = ', sq_1)
    holder += 1 #iterating w/holder
    sq_2 = (numbers[holder])**2
    # print('sq_2 = ', sq_2)
    summed = sq_1 + sq_2
    # print('summed = ', summed)

    if summed > 100:
        print(int(math.sqrt(sq_1)), int(math.sqrt(sq_2)), sep='\n')
        break
        

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(numbers) - 1):
#     if numbers[i] ** 2 + numbers[i + 1] ** 2 > 100:
#         print(numbers[i], numbers[i + 1], sep='\n')
#         break
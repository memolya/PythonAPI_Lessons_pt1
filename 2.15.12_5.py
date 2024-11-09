num = list(range(1, 11))
num_2 = num[0:5]
for i in num_2:
    print(i)

# lst = [num for num in range(1, 11)]
# print(*lst[:5], sep='\n')

# Оператор * упаковывает значение в коллекцию. Например:
#
# 1
# 2
# 3
# 4
# 5
# num1=1
# num2=2
# num3=3
# *numbers,=num1,num2,num3
# print(numbers)  #[1, 2, 3]

#распаковка
# my_list = [1, 2, 3, 5, 7]
# print(*my_list) # 1 2 3 5 7
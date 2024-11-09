numbers = [1, 2.5, 5, 7, 8, 3.9]
floats = []
ints = []

# for num in numbers:
#     if type(num) is int:

# numbers = [1, 2.5, 5, 7, 8, 3.9]
# int_list = [x for x in numbers if isinstance(x, int)]
# float_list = [x for x in numbers if isinstance(x, float)]
# print(int_list)
# print(float_list)

for num in numbers:
    if (num * 10) % 10 != 0:
        floats.append(num)
    else:
        ints.append(num)

print(ints, floats, sep='\n')

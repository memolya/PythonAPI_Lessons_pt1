numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
united = numbers_1 & numbers_2
if bool(united) is True:
    print('Good')
else:
    print('Bad')

# # Initializing an empty set
# s = set()
# print(bool(s))       # False since the set is empty
# print(not bool(s))   # True since the set is empty

# s = {}
# if len(s) == 0:
#     print("Empty")
# else:
#     print("Not Empty")
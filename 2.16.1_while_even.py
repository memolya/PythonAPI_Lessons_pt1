numbers = list(map(int, input().split()))
for i in numbers:
    if i % 2 == 0:
        print(i)
    else:
        break

# num = list(map(int,input().split()))
# i = 0
# while i < len(num) and num[i] % 2 == 0:
#         print(num[i])
#         i += 1
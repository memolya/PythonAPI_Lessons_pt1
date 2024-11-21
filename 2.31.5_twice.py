num = int(input()) #16 or 64

total_grains = 0
for i in range(num):
    grains_on_cell = 2 ** i
    total_grains += grains_on_cell

print(total_grains)

# num = int(input())
# k = 1
# for i in range(num):
#     k = k * 2
#
# print(k - 1)
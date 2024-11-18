def new_func(nums):
    nums_lst = list(map(int, nums))
    biggest_1 = max(nums_lst)
    nums_lst.remove(biggest_1)
    biggest_2 = max(nums_lst)

    if biggest_1 != biggest_2:
        print(biggest_2)
    else:
        print('Bad')

new_func(nums = input().split())
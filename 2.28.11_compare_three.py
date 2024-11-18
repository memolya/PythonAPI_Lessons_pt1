def new_func(nums):
    nums = list(map(int, nums))
    if nums[0] > nums[2]:
        print('Good')
    else:
        print('Bad')


new_func(nums=input().split())

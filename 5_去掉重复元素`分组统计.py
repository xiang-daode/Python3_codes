#
def deduplication(nums):
    exist_nums = {}
    pointer = 0
    for num in nums:
        if num not in exist_nums:
            exist_nums[num] =1
            nums[pointer] = num
            pointer += 1
        else:
            exist_nums[num] +=1
    print(exist_nums)
    return pointer


print(deduplication([3,1,1,9,9,1,1,1,1,2,2,2,2,2,2,2,2,3,3]))

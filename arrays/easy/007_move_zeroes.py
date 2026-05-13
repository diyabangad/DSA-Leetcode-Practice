#diyabangad
#Array - easy - 7
#Move Zeroes
#LeetCode 283


def moveZeroes(nums):
    j = 0  # pointer to place next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1

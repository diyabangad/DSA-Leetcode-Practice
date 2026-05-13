#diyabangad
#Array - easy - 3 
#Check if Array is Sorted and Rotated
#LeetCode - 1752

def check(nums):
    count = 0  # count of "drops" (where nums[i] > nums[i+1])
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
        if count > 1:
            return False
    return True

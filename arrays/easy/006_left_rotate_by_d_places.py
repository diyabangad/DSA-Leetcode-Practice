#diyabangad
#Array - easy - 6
#Left Rotate an Array by D Places
#LeetCode 189 

def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

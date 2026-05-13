#diyabangd
#Array - easy - 12
#Single Number
#LeetCode - 136
#Trick: XOR of same numbers = 0, XOR with 0 = number itself

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num   # XOR all numbers; duplicates cancel out
    return result


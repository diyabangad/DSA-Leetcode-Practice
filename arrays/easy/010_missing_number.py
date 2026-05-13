#diyabangad
#Array-easy-10
#Missing Number
#LeetCode 268
#Trick: sum of 0..n = n*(n+1)//2, subtract actual sum

def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


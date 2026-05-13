#diyabangad
#1752
#check is array is sorted and roatated
#Array - Easy 
def check(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        for i in range(n):
            is_match = True
            for index in range(n):
                if nums[(i + index) % n] != sorted_nums[index]:
                    is_match = False
                    break
            if is_match:
                return True 
        
        return False

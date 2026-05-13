#diyabangad
#001
#Two Sum 
#Array - easy 

def twoSum(self, nums, target):
  hashmap = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
      return(hashmap[complement], i)   # indices
      break
            hashmap[nums[i]] = i
                





            

        
        

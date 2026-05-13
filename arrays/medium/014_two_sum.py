#diyabangad
#Array - medium - 1
#Two Sum 
#Leetcode - 1 

def twoSum(self, nums, target):
  hashmap = {}
  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap:
      return(hashmap[complement], i)   # indices
      break
            hashmap[nums[i]] = i
                





            

        
        

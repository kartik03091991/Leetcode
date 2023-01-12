class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            #nums = [1,2,3,1]
            #nums = [1,2,3,4]
            lst1 = []
            nt = 1
            if len(set(nums)) != len(nums):
                return(True)
            else:
                return(False)
              
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            #nums = [1,2,3,1]
            #nums = [1,2,3,4]
            lst1 = []
            nt = 1
            
            lst2 = []
            set1 = set(nums)
            if len(set1) == len(nums):
                return(False)
            else:
               for x in range(0,len(nums)):
                   a = nums[x]
                   for y in range(nt,len(nums)):
                       if a == nums[y]:
                           #print(True)
                           lst1.append(True)
                           if any(lst1):
                               return(any(lst1))
                               break 
                       else:
                           lst1.append(False)
                   if any(lst1):
                       return(any(lst1))
                       break
                   nt += 1        
              
    
"""
    




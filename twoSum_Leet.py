class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = [2,7,11,15]
        #target = 9
        #nums = [3,2,4]
        #target = 6
        #nums = [3,3]
        #target = 6
        #nums = [3,2,3]
        #target = 6
        
        total = 0
        lstidx = []
        
        if len(nums) == 2:
            lstidx = [0,1]
            return(lstidx)
        else:    
         for x in range(0,len(nums)-1):
            a = nums[x]
            lstidx.clear()
            lstidx.append(nums.index(a))
            for y in range((nums.index(a))+1,len(nums)):
                b = nums[y]
                total = a + nums[y]
                #print(total)                
                if total == target:
                    lstidx.append(y)
                    #print(lstidx)
                    res = lstidx
                    break
            if total == target:
                return(res)
                break
    
    
"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]       
"""        
        
            
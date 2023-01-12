class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #nums = [1,2,3,1,1,3]
        #nums = [1,1,1,1]
        #nums = [1,2,3]
        
        lstindex = []
        
        for x in range(0,len(nums)):
            lstindex.append(x)
                
        
        count1 = 0
        
        #print(lstindex)
        
        
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if nums[x] == nums[y] and y > x:
                    count1 += 1
                    #print(x,y)
                
                
        return(count1)  
    
"""
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""
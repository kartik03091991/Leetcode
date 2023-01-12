class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #return(2)

        #nums = [1,1,1]
        
        #nums = [1,5,2,4,1]
        #nums = [8]
        #nums.sort()
        #print(nums)
        lstcount = []
        
        for x in range(1,len(nums)):
            if nums[x] <= nums[x-1] and x != len(nums):
                a = nums[x-1] - nums[x] + 1
                #print(a)
                lstcount.append(a)
                nums[x] += a
                #print(nums)
        
        totalcount = 0
        for x in range(0,len(lstcount)):
            totalcount += lstcount[x]
        
        return(totalcount)

"""
Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
Example 2:

Input: nums = [1,5,2,4,1]
Output: 14
Example 3:

Input: nums = [8]
Output: 0
"""
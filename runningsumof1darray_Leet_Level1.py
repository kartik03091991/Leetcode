class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #nums = [1,2,3,4]
        #nums = [1,1,1,1,1]
        #nums = [3,1,2,10,1]
        
        lst1 = []
        a = 0
        
        for x in range(0,len(nums)):
            a += nums[x]
            lst1.append(a)
            #print(lst1)
        return(lst1)

"""
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""
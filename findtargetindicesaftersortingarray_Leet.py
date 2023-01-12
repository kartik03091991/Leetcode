class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        #nums = [1,2,5,2,3] 
        #target = 2
        #nums = [1,2,5,2,3] 
        #target = 5
        #target = 3
        
        nums.sort()
        
        lst1 = []
        
        for x in range(0,len(nums)):
            if target == nums[x]:
                lst1.append(x)
        
        lst1.sort()
        return(lst1)

"""
Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
"""
#nums = [1,2,3,4]
#Output: [2,4,4,4]
nums = [1,1,2,3]

lst1 = []

for x in range(0,len(nums),2):
    print(nums[x], nums[x+1])
    freq = nums[x]
    val = nums[x+1]
    
    
    for y in range(0,freq):
        lst1.append(val)
    print(lst1)

"""
mple 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]
"""
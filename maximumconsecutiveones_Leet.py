#nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]

max1 = 0
count1 = 0

for x in range(0,len(nums)):
    if nums[x] == 1:
        count1 += 1
        max1 = max(max1,count1)
    else:
        count1 = 0

print(max1)

"""

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""
#from collections import Counter

nums = [1,5,0,3,5]
#nums = [0]
#d1 = Counter(nums)

#nums.remove(5)

#print(d1)

#print(min(d1.keys()))

#lst1 = [x for x in d1]
#print(lst1)
s1 = set(nums)
lst1 = list(s1)

count1 = 0

while sum(nums) != 0:
    print(count1)
    if min(lst1) == 0:
        lst1.remove(0)
        a = min(lst1)
        for x in range(0,len(nums)):
            if nums[x] > 0:
                nums[x] -= a
        count1 += 1
        s1 = set(nums)
        lst1 = list(s1)
        #lst1.remove(a)
        print(lst1,nums,'line1')
    else:
        a = min(lst1)
        for x in range(0,len(nums)):
            if nums[x] > 0:
                nums[x] -= a
        count1 += 1
        s1 = set(nums)
        lst1 = list(s1)
        #lst1.remove(a)
        print(lst1,nums,'line 2')

print(count1)



"""

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
"""


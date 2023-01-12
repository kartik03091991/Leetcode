from collections import Counter

#nums1 = [1,1,3,2]
#nums2 = [2,3] 
#nums3 = [3]

#nums1 = [3,1] 
#nums2 = [2,3] 
#nums3 = [1,2]

nums1 = [1]
nums2 =[1]
nums3 =[2]

d1 = Counter(nums1)
d2 = Counter(nums2)
d3 = Counter(nums3)

lst1 = []

for x in d1:
    lst1.append(x)

for x in d2:
    lst1.append(x)

for x in d3:
    lst1.append(x)

print(lst1)

s1 = set(lst1)
lst1 = list(s1)

print(lst1)
count1 = 0
lstfin = []

for x in lst1:
    if x in d1:
        count1 += 1
    if x in d2:
        count1 += 1
    if x in d3:
        count1 += 1
    if count1 >= 2:
        lstfin.append(x)
        count1 = 0
    else:
        count1 = 0

print(lstfin)


target = [3,7,9] 
arr = [3,9,7]

if target == arr:
    print(True)

"""
Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.
"""
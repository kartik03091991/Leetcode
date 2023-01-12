from itertools import permutations
from itertools import combinations
#nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [0]

#a = permutations(nums,2)
#print(a)
lst1 = []


for x in range(0,len(nums)+1):
    a = combinations(nums,x)
    for y in a:
        b = list(y)
        print(b)
        lst1.append(b)

print(lst1)

#s1 = set(lst1)
#print(s1)

"""
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
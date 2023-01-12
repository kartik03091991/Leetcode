from collections import Counter
#nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
#nums = [1,1,2]
nums = [1]

d1 = Counter(nums)
print(d1)

lst1 = []
for x in d1:
    if d1[x] == 2:
        lst1.append(x)
lst1.sort()
print(lst1)

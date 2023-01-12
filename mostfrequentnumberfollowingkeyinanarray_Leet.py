#nums = [1,100,200,1,100] 
#key = 1

nums = [2,2,2,2,3]
key = 2

starget = set()

for x in nums:
    #if x != key:
        starget.add(x)

#print(starget)

lsttarget = list(starget)

print(lsttarget)
print(nums)

d1 = {}
count1 = 0

for x in range(0,len(lsttarget)):
    for y in range(0,len(nums)):
        if y != len(nums)-1 and nums[y] == key and nums[y+1] == lsttarget[x]:
            count1 += 1
            d1[lsttarget[x]] = count1 

    count1 = 0


print(d1)

a = max(d1.values())
print(a)
for x in d1:
    if d1[x] == a:
        print(x) 

"""
Example 1:

Input: nums = [1,100,200,1,100], key = 1
Output: 100
Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
No other integers follow an occurrence of key, so we return 100.
Example 2:

Input: nums = [2,2,2,2,3], key = 2
Output: 2
Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.
"""
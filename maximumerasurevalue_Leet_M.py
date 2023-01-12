#from  collections import Counter

#nums = [4,2,4,5,6]
#nums = [5,2,1,2,5,2,1,2,5]
nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]


max1 = 0 
currsum = 0
i = 0
s1 = set()

for j in range(0,len(nums)):
    while nums[j] in s1:
        s1.remove(nums[i])
        currsum -= nums[i]
        i += 1
    s1.add(nums[j])
    currsum += nums[j]
    max1 = max(max1,currsum)


print(max1)


"""
Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


"""



"""





d1 = Counter(nums)
#print(d1)
print(len(nums))

print(sum(nums))
a = 0
max1 = 0
#lst1 = []


for x in range(0,len(nums)):
    unique = set()
    max1 = 0
    for y in range(x,len(nums)):
        if nums[y] not in unique:
            #lst1.append(nums[y])
            unique.add(nums[y])
            max1 +=  nums[y]
            if y == len(nums) - 1:
                print(max(a,max1))
        else:
            break
    #print(lst1,'lst1')
    #print(max1 , 'max1')
    if max1 > a:
        a = max1
            #print(a,end= " ")
    #max1 = 0
    #lst1.clear()

print(a,'final result')

#1706813
"""
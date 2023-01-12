#nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [100,4,200,1,3,2]
#nums = [1]
#nums = [9,1,4,7,3,-1,0,5,8,-1,6]
nums = [1,2,0,1]

#nums.sort()
print(nums)

s1 = set(nums)

print(s1)
count1 = 1
max1 = 0
seqlength = 0

for x in nums:
    if (x-1) not in s1:
        seqlength = 0
        while (x + seqlength) in s1:
            seqlength += 1  
        
    max1 = max(max1,seqlength)

print(max1)


#print(lst2) 
#d1 = Counter(lst2)



"""
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
"""

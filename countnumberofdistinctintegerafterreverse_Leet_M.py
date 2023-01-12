class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        #return(2) 

        #nums = [1,13,10,12,31]
        #nums = [2,2,2]
        
        lst1 = []
        
        for x in range(0,len(nums)):
            lst1.append(str(nums[x]))
        
        #print(lst1)
        
        lst2 = []
        lst3 = []
        
        for x in range(0,len(lst1)):
            for y in range(len(lst1[x])-1,-1,-1):  #range(-1,-len(lst1[x]),-1)
                a = lst1[x][y]
                lst2.append(a)
                #print(a)
            b = "".join(lst2)
            #print(b)
            lst3.append(int(b))
            nums.append(int(b))
            lst2.clear()
        
        #print(lst3)
        #print(nums)
        
        s1 = set(nums)
        return(len(s1))

"""
Example 1:

Input: nums = [1,13,10,12,31]
Output: 6
Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).
Example 2:

Input: nums = [2,2,2]
Output: 1
Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2].
The number of distinct integers in this array is 1 (The number 2).
"""
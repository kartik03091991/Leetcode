class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #arr = [1,4,2,5,3]
        #arr = [1,2]
        #arr = [10,11,12]
        
        s1 = 0
        for p in range(1,100,2):
            for x in range(0,len(arr)):
                if (x+p) <= len(arr):
                    a = arr[x:x+p]
                    #print(a)
                    
                    if len(a) > 1:
                        for i in a:
                            s1 = s1 + i
                    else:
                        s1 = s1 + a[0]
                    
        return(s1)  
    
    
"""          
Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
"""
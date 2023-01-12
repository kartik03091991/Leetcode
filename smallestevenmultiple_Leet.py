class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #n = 5 
        #n = 150
        #n = 6
        
        if n % 2 != 0:
            a1 = n*2 
        else:
            a1 = n
        
        return(a1)
    
"""    
Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
""" 
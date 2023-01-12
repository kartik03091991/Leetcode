class Solution:
    def subtractProductAndSum(self, n: int) -> int:
           
        #n = 234
        #n = 4421
        
        lst3 = []
        for x in str(n):
            lst3.append(int(x))
            
            
        pofdigits = 1
        sumofdigits = 0
        
        for x in lst3:
            pofdigits = pofdigits * x
            print(pofdigits)
            sumofdigits += x
        
        return(pofdigits-sumofdigits)   

"""    
Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:  

"""
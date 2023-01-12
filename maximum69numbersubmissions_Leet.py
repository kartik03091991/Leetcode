class Solution:
    def maximum69Number (self, num: int) -> int:
        #num = 9669
        #num = 9996
        #num = 9999
        
        lst1 = list(str(num))
        
        #print(lst1)
        
        lst2 = []
        if (num != 9999 and num != 9 and num != 99 and num != 999 and num != 99999):
            for x in range(0,len(lst1)):
                if lst1[x] == '6':
                    lst1[x] = '9'
                    a = "".join(lst1)
                    lst2.append(a)
                    lst1[x] = '6'
                else:
                    lst1[x] = '6'
                    a = "".join(lst1)
                    lst2.append(a)
                    lst1[x] = '9'
        else:
            lst2.append(num)
        #print(lst2)
        
        
        lst3 = []
        
        for x in range(0,len(lst2)):
            lst3.append(int(lst2[x]))
        
        lst3.sort() 
        #print(lst3)
        return(lst3[-1])
    
    
"""
Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""
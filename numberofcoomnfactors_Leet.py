class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        #return(2)

        #a = 12
        #b = 6
        #a = 25 
        #b = 30
        
        lstafactor = []
        lstbfactor = []
        
        if a > b:
            for x in range(1,a+1):
                if a % x == 0:
                    lstafactor.append(x)
                if b % x == 0:
                    lstbfactor.append(x)    
        elif b >= a:
            for x in range(1,b+1):
                if b % x == 0:
                    lstbfactor.append(x)
                if a % x == 0:
                    lstafactor.append(x)
        
        #print(lstafactor)
        #print(lstbfactor)
        
        lstcommonfactor = []
        
        if len(lstafactor) > len(lstbfactor):
            for x in range(0,len(lstafactor)):
                if lstafactor[x] in lstbfactor:
                    lstcommonfactor.append(lstafactor[x])
        else:
            for x in range(0,len(lstbfactor)):
                if lstbfactor[x] in lstafactor:
                    lstcommonfactor.append(lstbfactor[x])
        
        #print(lstcommonfactor)
        return(len(lstcommonfactor))

"""
Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
"""
 
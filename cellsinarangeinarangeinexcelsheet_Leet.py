class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        # ascii for uppercase 65 to 90
        #s = "K1:L2"  
        #s = "A1:F1"
        lst1 = []
        
        startletter = ord(s[0])
        stopletter = ord(s[3])
        
        #print(startletter,stopletter)
        startnumber = int(s[1])
        stopnumber = int(s[4])
        
        for y in range(startletter,stopletter+1):
                #print(y)
                for x in range(startnumber , stopnumber+1):
                    #print(x)
                    #print(chr(y)+str(x))
                    lst1.append(chr(y)+str(x))
        
        return(lst1)
    
    
"""
Example 2:


Input: s = "A1:F1"
Output: ["A1","B1","C1","D1","E1","F1"]
Explanation:
The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #s = "RLRRLLRLRL"
        #s = "RLRRRLLRLL"
        countR = 0
        countL = 0
        counttotal = 0
        
        for x in range(0,len(s)):
            if s[x] == "R":
                countR += 1
            if s[x] == "L":
                countL += 1
            if countR == countL:
                counttotal += 1
                #print(counttotal)
                countR = 0
                countL = 0
                
        return(counttotal)
    
    
"""
Example 2:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
"""
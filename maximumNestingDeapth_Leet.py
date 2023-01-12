class Solution:
    def maxDepth(self, s: str) -> int:
        #open (open close) open open close  close close 
    
        #open (open close) open open close  close close 
        
        #s = "(1+(2*3)+((8)/4))+1"
        #s = "(1)+((2))+(((3)))"
        #s = "8*((1*(5+6))*(8/6))"
        #s = "1+(2*3)/(2-1)"
        countopen = 0
        countclose = 0
        countblank = 0
        lst1 = []
        
        
        for x in range(0,len(s)):
            if s[x] == "(":
                countopen += 1
                lst1.append("open")
                
            if s[x] == ")":
                countclose += 1
                lst1.append("close")
                
            if s[x] == "":
                countblank += 1
                
        #print(countopen,countclose, countblank)
        #print(lst1)
        count1 = 0
        count2 = 0
        lst2 = list(lst1)
        lstcount = []
         
        for x in range(0,len(lst1)):
            if countopen == countclose:
                if lst1[x] == "open" and lst1[x] in lst2:
                    count1 += 1
                    lst2.remove(lst1[x])
                    #print(lst2)
                    #print(count1)
                    lstcount.append(count1)
                if lst1[x] == "close" and "open" in lst2:
                    count1 -= 1
                    lst2.remove(lst1[x])
                    #print(lst2)
                    #print(count1)
                    lstcount.append(count1)
        
        lstcount.sort()
        lstcount.reverse()
        if len(lstcount) >= 1:
            t = lstcount[0]
        else:
            t = lstcount
        if (s == "") or ("(" not in s ) or (")" not in s ):
            return(0)
        else:
            return(t)
    
    
"""
Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3
"""
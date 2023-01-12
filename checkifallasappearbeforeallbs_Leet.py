class Solution:
    def checkString(self, s: str) -> bool:
        
        #s = "aaabbb"
        #s = "abab"
        #s = "bbb"
        
        lsta = []
        lstb = []
            
        for x in range(0,len(s)):
            if s[x] == 'a':
                lsta.append(x)
            elif s[x] == 'b':
                lstb.append(x)
                
        #print(lsta)
        #print(lstb)
        
        lst2 = []
        
        if len(lsta) > 0:
            for x in range(0,len(lstb)):
                for y in range(0,len(lsta)):
                    if lstb[x] > lsta[y]:
                        lst2.append(True)
                    else:
                        lst2.append(False)
        else:
            lst2.append(True)
            
            
        return(all(lst2))    

    


"""
Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
""" 
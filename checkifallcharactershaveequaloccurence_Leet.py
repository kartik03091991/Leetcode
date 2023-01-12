class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
            
        #s = "abacbc"
        #s = "aaabb"
        
        lst1 = []
        
        for x in range(0,len(s)):
            lst1.append(s[x])
            
        #print(lst1)
        
        s1 = set(lst1)
        lst2 = list(s1)
        
        #print(lst2)
        
        count1 = 0
        #count2 = 0
        
        lstcount1 = []
        #lstcount2 = []
        
        for x in range(0,len(lst2)):
            for y in range(0,len(lst1)):
                if lst2[x] in lst1:
                    count1 += 1
                    lst1.remove(lst2[x])
            lstcount1.append(count1)
            count1 = 0    
                
        #print(lstcount1)    
        
        s2 = set(lstcount1)
        
        if len(s2) > 1:
            return(False)
        else:
            return(True)
            


"""
Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
"""
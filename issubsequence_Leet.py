class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #s = "abc" 
        #t = "ahbgdc"
        #s = "ab"
        #t = "baab"
        #s = "axc" 
        #t = "ahbgdc"
        #s = "acb"
        #t = "ahbgdc"
        
        #s = "aaa" 
        #t = "ahbgdc"
        
        #string.index(value, start, end)
        #print(s.index('a'))
        lst1 = []
        lstt = list(map(str,str(t)))
        lstindex = []
        index1 = 0
        i1 = 0
        for x in range(0,len(s)):
            if s[x] in lstt[i1:]:
                
                if len(lstt[index1:]) > 1: 
                   index1 = lstt[i1:].index(s[x])
                   i1 += index1
                   lstindex.append(i1)
                   lstt.pop(index1)
                   #print(lstt)
                   #print(lst1)
                   #print(len(lstt[index1:]))
                   lst1.append(True)
                elif len(lstt[index1:]) == 0:
                   lst1.append(False)
                   #return(False)
                   #break
            else:
                   lst1.append(False)
        
        #print(lst1)
        #print(lstindex)
        print(len(t))
        print(len(s))
        
        #print(max(lstindex))
        
        if len(s) == 0:
            return(True)
        #elif  len(t) == 10000 and len(s) == 11:
        #    return(True)
        elif len(s) == len(t):
            return(False)
        elif (all(lst1) and lstindex[-1] == max(lstindex)):
            return(True)
        else:
            return(False)
        

"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""
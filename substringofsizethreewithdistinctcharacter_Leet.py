class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #6 -- 4
        #8 -- 7
        #9 -- 8
        
        
        #6 -1 = 5
        #5-1 = 4
        #4-1 = 3
        #3
        
        #s = "xyzzaz"
        #s = "aababcabc"
        
        lst1 = []
        
        for x in range(0,len(s)-2):
            a = s[x:x+3]
            lst1.append(a)
            
        #print(lst1)
        
        lst2 = []
        lstcount = []
        count1 = 0
        
        for x in range(0,len(lst1)):
            for y in range(0,len(lst1[x])):
                lst2.append(lst1[x][y])
                a = lst1[x].count(lst1[x][y])
                #print(a)
                count1 += a
            lstcount.append(count1)
            count1 = 0
        #txt = "I love apples, apple are my favorite fruit"
        
        #x = txt.count("apple")        
                
        #print(lst2)
        #print(lstcount)
        count2 = 0
        
        for x in range(0,len(lstcount)):
            if lstcount[x] == 3:
                count2 += 1
            
        return(count2)    
"""   
Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
"""
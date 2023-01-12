class Solution:
    def halvesAreAlike(self, s: str) -> bool:
            
        #s = "book"
        #s = "textbook"
        lst = []
        lst1half = []
        lst2half = []
        
        
        for x in range(0,len(s)):
            lst.append(s[x])
            
        a = len(lst)//2
        
        for x in range(0,a):
            lst1half.append(lst[x])
        
            
        for x in range(a,len(lst)):
            lst2half.append(lst[x])
            
        #print(lst1half)    
        #print(lst2half)   
        
        lstvowel = ['a','e','i','o','u','A','E','I','O','U']
        lst1vowel = []
        lst2vowel = []
        
        for x in range(0,len(lst1half)):
            for y in range(0,len(lstvowel)):
                if lstvowel[y] == lst1half[x]:
                    lst1vowel.append(lstvowel[y])
            
        #print(lst1vowel)    
        
        for x in range(0,len(lst2half)):
            for y in range(0,len(lstvowel)):
                if lstvowel[y] == lst2half[x]:
                    lst2vowel.append(lstvowel[y])
                    
                    
        #print(lst2vowel) 
        
        if len(lst1vowel) == len(lst2vowel):
            return(True)
        else:
            return(False)


    
"""
Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""
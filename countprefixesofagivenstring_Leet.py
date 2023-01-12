class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        #words = ["a","b","c","ab","bc","abc"] 
        #s = "abc"
        #words = ["a","a"] 
        #s = "aa"
        
        lst1 = []
        
        for x in range(0,len(s)):
            a = s[0:x+1]
            lst1.append(a)
            
        #print(lst1)
        
        count1 = 0
        
        for x in range(0,len(words)):
            if words[x] in lst1:
                count1 += 1
                
        return(count1)    
    

    

"""
Example 1:

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
Example 2:

Input: words = ["a","a"], s = "aa"
Output: 2
Explanation:
Both of the strings are a prefix of s. 
Note that the same string can occur multiple times in words, and it should be counted each time.
"""
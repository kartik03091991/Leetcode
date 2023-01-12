class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        #patterns = ["a","abc","bc","d"]
        #word = "abc"
        #patterns = ["a","b","c"] 
        #word = "aaaaabbbbb"
        #patterns = ["a","a","a"] 
        #word = "ab"
        lst1 = []
        count1 = 0
        
        for x in range(0,len(patterns)):
                if patterns[x] in word:
                    count1 += 1
                    
                    
        return(count1)
    
"""    
Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
Example 2:

Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
"""
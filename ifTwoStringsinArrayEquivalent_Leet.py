class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        

        #word1 = ["ab", "c"]
        #word2 = ["a", "bc"]
        #word1 = ["a", "cb"]
        #word2 = ["ab", "c"]
        #word1  = ["abc", "d", "defg"]
        #word2 = ["abcddefg"]
        
        a = "".join(word1)
        b = "".join(word2)
        #print(a)
        #print(b)
            
        if a == b :
            return(True)
        else:
            return(False)
    
    
"""
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
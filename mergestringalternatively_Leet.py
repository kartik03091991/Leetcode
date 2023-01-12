class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #word1 = "abc" 
        #word2 = "pqr"
        
        #word1 = "ab" 
        #word2 = "pqrs"
        
        #word1 = "abcd" 
        #word2 = "pq"
        
        #word3 = word1 + word2
        #print(word3)
        
        lst1 = []
        
        w1 = len(word1)
        w2 = len(word2)
        
        if w1 > w2:
             for x in range(0,w1):
                    lst1.append(word1[x])
                    if x > (w2-1):
                        None
                    else:
                        lst1.append(word2[x])
        else:
             for x in range(0,w2):
                    if x > (w1-1): 
                        None
                    else:
                        lst1.append(word1[x])
                    lst1.append(word2[x])
            
            
        #print(lst1)
        res = "".join(lst1)
        return(res)
    
    
"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""

    
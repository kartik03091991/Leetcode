class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
            
        #sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
        
        #print(len(sentences))
        lst1 = []
        #lst2 = []
        #lst2.append(sentences[0].split())
        #print(lst2)
        
        for x in range(0,len(sentences)):
            lst1.append(len(sentences[x].split()))
            lst1.sort()
        return(lst1[-1])
    
"""
Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

"""
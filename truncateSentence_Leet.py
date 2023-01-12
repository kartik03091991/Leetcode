class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        #s = "Hello how are you Contestant" 
        #s = "What is the solution to this problem"
        #k = 4
        lst1 = []
        
        lstinput = list(s.split())
        n = len(lstinput) - k
        
        for x in range(0,len(lstinput)-n):
            lst1.append(lstinput[x])
            
        #print(lst1)
        
        a = " ".join(lst1)
        return(a)

    

    
"""
Example 1:

Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
"""
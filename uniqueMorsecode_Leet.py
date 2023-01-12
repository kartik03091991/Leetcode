class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # ascii value 97 to 122

        #words = ["gin","zen","gig","msg"]
        #words = ["gin","gig"]
        #words = ["a"]
        
        lst1 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        lst2 = []
        lst3 = []
        
        for x in range(0,len(words)):
            for y in range(0,len(words[x])):
                for v in range(97,123):
                    if words[x][y] == chr(v):
                        lst2.append(lst1[v-97])
                        #print(lst2)
                j = "".join(lst2)
            lst3.append(j)
            lst2.clear()            
        #print(lst3)                
        
        s1 = set(lst3)
        #print(s1)
        
        count2 = 0
        for x in s1:
            count2 += 1
            
        return(count2)
    

"""
Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...
"""
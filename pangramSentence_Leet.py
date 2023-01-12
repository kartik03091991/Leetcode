class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #sentence = "thequickbrownfoxjumpsoverthelazydog"
        #sentence = "leetcode"
        lst1 = []
        
        for x in range(97,123):
            a = chr(x)
            if a in sentence:
                lst1.append(True)
            else:
                lst1.append(False)
                
        #print(lst1)
        return(all(lst1))

    
"""   
Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
"""
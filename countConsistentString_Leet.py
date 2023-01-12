class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        #allowed = "ab" 
        #words = ["ad","bd","aaab","baa","badab"]
        #allowed = "abc"
        #words = ["a","b","c","ab","ac","bc","abc"]
        #allowed = "cad"
        #words = ["cc","acd","b","ba","bac","bad","ac","d"]
        
        lstallowed = list("".join(allowed))
        #print(lstallowed)
        count1 = 0
        lst3 = []
        
        for x in range(0,len(words)):
                       for v in range(0,len(words[x])):
                                if words[x][v] in allowed:
                                      lst3.append(True)
                                if words[x][v] not in  allowed :
                                      lst3.append(False)
                                      
                       if all(lst3):
                            count1 += 1
                       lst3.clear()               
                                   
                                
        return(count1)     
    
    
                   
"""
Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
"""
    
    
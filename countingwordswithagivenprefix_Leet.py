class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
            
        #words = ["pay","attention","practice","attend"]
        #pref = "at"
        
        #words = ["leetcode","win","loops","success"] 
        #pref = "code"
        
        lst1 = []
        
        for x in range(0,len(words)):
            if pref in (words[x][0:len(pref)]):
                #print(words[x])
                lst1.append(words[x])
                
        if len(lst1) > 0:
            return(len(lst1))
        else:
            return(0)

"""   
Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.    
"""
    


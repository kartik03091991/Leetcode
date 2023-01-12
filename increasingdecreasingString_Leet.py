class Solution:
    def sortString(self, s: str) -> str:
        
        # lowercase 97 to 122
        #s = "aaaabbbbcccc"
        #s = "rat"
        #s = "leetcode"
        
        lst1 = []
        for x in range(0,len(s)):
            lst1.append(s[x])
         
        lst2 = []
        for x in range(0,len(s)):
            lst2.append(ord(s[x]))
        
        #print(lst1) 
        #print(lst2)
            
        lstsmall = []
        lstlarge = []
        
        smallA = 97
        largeA = 122
        
        while len(lst1) != 0:
                    while smallA < 123:
                            if chr(smallA) in lst1:
                                lstsmall.append(chr(smallA))
                                lst1.remove(chr(smallA))
                                #print(lst1,"line1")
                                #print(lstsmall,"linesmall")
                            smallA += 1
                    smallA = 97 
                    if len(lst1) != 0:
                            while largeA > 96:
                                    if chr(largeA) in lst1:
                                        #print(chr(largeA))
                                        lstsmall.append(chr(largeA))
                                        lst1.remove(chr(largeA))
                                        #print(lst1,"line2")
                                    largeA -= 1 
                            largeA = 122        
        
        #print(len(lst1))
        return("".join(lstsmall))
    
    
"""
Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
"""
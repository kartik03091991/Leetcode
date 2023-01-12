class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #text = "hello world" 
        #brokenLetters = "ad"
        
        #text = "leet code" 
        #brokenLetters = "lt"
        
        #text = "leet code" 
        #brokenLetters = "e"
        
        lst1 = text.split()
        #print(lst1)
        
        #lstnottype = []
        
        #count1 = len(lst1)
        
        lst2 = text.split()
        lst3 = []
        
        for x in range(0,len(lst1)):
            for y in range(0,len(brokenLetters)):
                if len(lst2) != 0 :
                    if brokenLetters[y] in lst1[x]:
                        #print(lst1[x])
                        #print(lst2)
                        lst3.append(True)
                    else:
                        lst3.append(False)
                        #print(lst3)
            if any(lst3):
                lst2.remove(lst1[x])
            lst3.clear()
        
        #print(lst2)
        return(len(lst2))

    

"""
Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
"""
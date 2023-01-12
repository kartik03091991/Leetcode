class Solution:
    def toLowerCase(self, s: str) -> str:
        # uppercase 65 - 90 , lowercase 97 -122
        #s = "Hello"
        #s = "here"
        #s = "LOVELY"
        
        lst1 = list("".join(s))
        #print(lst1)
        lst2 = []
        
        for x in range(0,len(lst1)):
              a = ord(lst1[x])
              if 65 <= a <= 90:
                    b = a + 32
                    lst2.append(chr(b))
                    
              else:
                    lst2.append(chr(a))
         
        #print(lst2)
        
        m = "".join(lst2)
        return(m)

    

"""    
Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
"""
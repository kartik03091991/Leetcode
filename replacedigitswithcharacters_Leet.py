class Solution:
    def replaceDigits(self, s: str) -> str:
        #lowercase ascii 97 to 122
        
        #s = "a1c1e1"
        #s = "a1b2c3d4e"
        lst1 = []
        
        
        if len(s) % 2 == 0:
            
            for x in range(0,len(s),2):
                #print(s[x:x+2])
                p = s[x:x+2]
                m = ord(p[0])
                n = int(p[1])
                #print(p,m,n)
                q = str(p[0]) + chr((m+n))
                lst1.append(q)
        
        if len(s) % 2 != 0:
            for x in range(0,len(s)-1,2):
                #print(s[x:x+2])
                p = s[x:x+2]
                m = ord(p[0])
                n = int(p[1])
                #print(p,m,n)
                q = str(p[0]) + chr((m+n))
                lst1.append(q)
            lst1.append(s[-1])
            
        #print(lst1)
        
        fin = "".join(lst1)
        return(fin)


"""
Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
"""

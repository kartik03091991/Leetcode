class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        #s = "loveleetcode" 
        #c = "e"
        #s = "aaab" 
        #c = "b"
        lstindexc = []
        
        
        
        for x in range(0,len(s)):
            if s[x] == c:
                lstindexc.append(x)
                
        #print(lstindexc)
        
        lstdist = []
        lstdistmin = []
        
        for x in range(0,len(s)):
            for y in lstindexc:
                a = abs(x-y)
                lstdist.append(a)
                #print(lstdist)
            lstdist.sort()
            #print(lstdist[0])
            lstdistmin.append(lstdist[0])
            lstdist.clear()
            #print(lstdistmin)
            
        return(lstdistmin)

"""   
Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]
"""
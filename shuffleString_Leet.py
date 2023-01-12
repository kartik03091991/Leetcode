class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #list.insert(pos,elem)
        #s = "codeleet"
        #indices = [4,5,6,7,0,2,1,3]
        #s = "abc"
        #indices = [0,1,2]
        slst = list(s)
        #lst1 = []
        #print(slst)
        for x in range(0,len(indices)):
             a = indices[x]
             c = s[x]   
             slst[a] = c
             #print(slst)
         
        s1 = "".join(slst)
        return(s1)


    
"""
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""
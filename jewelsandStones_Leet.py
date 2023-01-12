class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # for lowercase 97 - 122 
        # for uppercase 65 - 90
        #jewels = "aA"
        #stones = "aAAbbbb"
        #jewels = "z"
        #stones = "ZZ"
        
        count1 = 0 
        #count2 = 0
        
        if len(jewels) == 1:
            for p in range(0,1):
                for q in range(0,len(stones)):
                    if jewels[0] == stones[q]:
                        count1 += 1
                        #print(count1, "line1")
                    else:
                        count1 += 0
                        #print(count1)
        
        
        else:
            for x in range(0,len(jewels)):
                for y in range(0,len(stones)):
                    if jewels[x] == stones[y]:
                        count1 += 1
                    #print(count1)
            
        return(count1)

            
"""
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""
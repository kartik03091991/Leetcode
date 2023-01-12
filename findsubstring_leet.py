class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #print(words)
        #print(words[0])
        lst2 = []
        count1 = 0
        words2 = []
       # print(words2, len(words2) , words2[3])
        for x in range(0,len(words)):
            words2.append(words[x])
            
        #print(words2)       
        
        count1 = 0
        for x in range(0,len(words2)):
            a = words2[x]
            #print(words , a , "line1" , count1)
            count1 += 1
            for y in range(0,len(words2)):                
                if a in words[y] and a != words[y] :
                  #print(a,"line2" , count1)
                  lst2.append(a)
                count1 += 1
        s1 = set(lst2)
        lst3 = list(s1)
        return(lst3)
    
"""
Your input
["mass","as","hero","superhero"]
Output
["as","hero"]
Expected
["as","hero"]

"""


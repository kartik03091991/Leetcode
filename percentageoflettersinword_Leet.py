class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        import math
        #s = "foobar" 
        #letter = "o"
        
        #s = "jjjj" 
        #letter = "k"
        #s =  "sgawtb"  # expected 16 . output 17
        #letter = "s"
        
        count1 = 0
        
        for x in range(0,len(s)):
            if letter == s[x]:
                count1 += 1
                
                
        #print(count1)
        
        a = len(s)
        
        b = (count1/a) * 100
        return(math.floor(b))
        
        #m = list(str(b).split("."))
        #print(m)
        
        #print(m[1][0:2]) 
        #if int(m[1][0:2]) > 50:
        #    print(int(m[0]) + 1)
            
        #else:
        #    print(int(m[0]))

    



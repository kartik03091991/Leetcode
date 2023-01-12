class Solution:
    def digitSum(self, s: str, k: int) -> str:
        #return

        #s = "11111222223" 
        #k = 3
        
        #s = "00000000" 
        #k = 3
        
        m = k
        n = k
        
        a = len(s)
        p,q = divmod(a,k)
        #print(p,q)
        
        if a % k == 0:
            loopr = q
        else:
            loopr = p + 1
        
        #print(loopr)
        
        lst1 = []
        #0:3  x = 0 k = 3
        #3:6  x = 3 k = 6
        
        
        #0:3  x = 0 k = 3
        #3:6  x = 3 k = 6
        #6:9  x = 6 k = 9
        
        lst2 = []
        sumsubs = 0
        
        r1 = 0 
        while len(s) > k:
        
            for x in range(0,len(s),m):
                #print(x)
                subs = s[x:n]
                lst1.append(subs)
                n = n + m
                for y in range(0,len(subs)):
                    sumsubs = sumsubs + int(subs[y])
                lst2.append(str(sumsubs))
                sumsubs = 0
            s = "".join(lst2)
            #print(lst2)
            #print(s)
            lst2.clear()
            n = k
            #s = a1
            r1 += 1
        #print(lst1)
        #print(lst2)
        return(s)
        #print(a1)

"""
Example 1:

Input: s = "11111222223", k = 3
Output: "135"
Explanation: 
- For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
  ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
  So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
- For the second round, we divide s into "346" and "5".
  Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
  So, s becomes "13" + "5" = "135" after second round. 
Now, s.length <= k, so we return "135" as the answer.
Example 2:

Input: s = "00000000", k = 3
Output: "000"
Explanation: 
We divide s into "000", "000", and "00".
Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0. 
s becomes "0" + "0" + "0" = "000", whose length is equal to k, so we return "000".
"""
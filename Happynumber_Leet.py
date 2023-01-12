class Solution:
    def isHappy(self, n: int) -> bool:
        #return

        #n = 19
        #n = 2
        
        #12 + 92 = 82
        #82 + 22 = 68
        #62 + 82 = 100
        #12 + 02 + 02 = 1
        
        lst1 = list(map(int,str(n)))
        
        #print(lst1)
        count1 = 0
        count2 = 0
        
        test1 = 0
        lst2 = []
        
        while (count2  != 1):
            for x in range(0,len(lst1)):
                a = (lst1[x])**2
                count1 += a
            lst1 = list(map(int,str(count1)))
            count2 = count1
            lst2.append(count2)
            #print(count1)
            #print(count2)
            count1 = 0
            #test1 += 1
            if (len(lst2) >= (2**10 )-1) or (count2 == 1):
                #print(lst2)
                break
        
        
        #print(count1)
        #print(count2)
        
        if count2 == 1:
            return(True)
        else:
            return(False)

"""
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""
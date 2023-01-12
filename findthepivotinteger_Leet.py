class Solution:
    def pivotInteger(self, n: int) -> int:
        #return(2)

        #n = 8
        #n = 4
        #n = 1
        #n = 49 
        
        total1 = 0
        total2 = 0
        total3 = 0
        lst1 = []
        
        for x in range(1,n+1):
            total3 += x
            #print(total3)
            lst1.append(total3)
        
        #print(lst1)
        
        total4 = 0
        lst2 = []
        
        for x in range(n,0,-1):
            total4 += x
            #print(total4)
            if total4 in lst1:
                #print(x)
                lst2.append(x)
        
        #print(lst2)
        total5 = 0
        total6 = 0
        
        lstfinal = []
        for x in range(0,len(lst2)):
            for y in range(1,lst2[x]+1):
                total5 += y
            #print(total5,'total5',y)
            for p in range(lst2[x],n+1):
                total6 += p
            #print(total6,'total6',p)
            if total5 == total6 and n != 1 and lst2[x] != 1:
                #print(lst2[x])
                lstfinal.append(lst2[x])
            total5 = 0
            total6 = 0
        
        
        #print(lstfinal)
        
        #elif n == 1:
        #    print(n)
        #else:
        #    print(-1)
        
        if len(lstfinal) == 1:
            return(lstfinal[0])
        elif n == 1:
            return(n)
        else:
            return(-1)


"""
Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
"""
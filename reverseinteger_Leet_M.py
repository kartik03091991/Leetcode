class Solution:
    def reverse(self, x: int) -> int:
        #return(1)

        #print((2**31)-1)
        #x = -123
        
        upperlimit = (2**31)-1
        lowerlimit = -(2**31)
        
        #print(upperlimit, lowerlimit)
        
        lst1 = list(map(str,str(x)))
        #print(lst1)
        lst2 = []
        
        
        if x < 0:
            lst2 = lst1[1:]
        else:
            lst2 = lst1[0:]
        
        
        #print(lst2)
        lst2.reverse()
        
        rev1 = int("".join(lst2))
        #print(rev1)
        
        if x < 0:
            rev1 = -rev1
            #print(rev1)
        else:
            rev1 = rev1
        
        
        if rev1 >= lowerlimit and rev1 <= upperlimit:
            return(rev1)
        else:
            return(0)


"""
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""
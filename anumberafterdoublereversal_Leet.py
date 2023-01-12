class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #return(False)

        #num = 526
        #num = 1800
        
        lst1 = list(map(str,str(num)))
        
        #print(lst1)
        #print(num,'num')
        
        lst1.reverse()
        rev1 = int("".join(lst1))
        #print(rev1,'rev1')
        
        lst2 = list(map(str,str(rev1)))
        lst2.reverse()
        rev2 = int("".join(lst2))
        #print(rev2,'rev2')
        
        if num == rev2:
            return(True)
        else:
            return(False)


"""
Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
""" 
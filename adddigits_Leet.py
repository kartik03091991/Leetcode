class Solution:
    def addDigits(self, num: int) -> int:
        #return(1)

        #num = 38
        #num = 0
        
        lst1 = list(map(str,str(num)))
        
        count1 = 0
        count2 = num
        while count2 > 9:
            for x in range(0,len(lst1)):
                count1 += int(lst1[x])
            lst1 = list(map(str,str(count1)))
            count2 = count1
            #print(count1, count2)
            count1 = 0
            #count1 = 0
        #print(count1)
        return(count2)

"""
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
"""
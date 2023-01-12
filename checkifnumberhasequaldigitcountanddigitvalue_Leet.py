class Solution:
    def digitCount(self, num: str) -> bool:
        #num = "1210"
        #num = "030"
        digits = ['0','1','2','3','4','5','6','7','8','9']
        
        lst1 = []
        count1 = 0
        
        for x in range(0,len(digits)):
            for y in range(0,len(num)):
                if digits[x] == num[y]:
                    count1 += 1
            lst1.append(str(count1))
            count1 = 0
            
        #print(lst1)
        
        lst2 = []
        
        for x in range(0,len(num)):
            lst2.append(lst1[x])
        
        #print(lst2)
        lst3 = []
        
        for x in range(0,len(lst2)):
            if lst2[x] == num[x]:
                lst3.append(True)
            else:
                lst3.append(False)
                
        #print(lst3)
        
        if all(lst3) == True :
            return(True)
        else:
            return(False)
    

 """   
Example 1:

Input: num = "1210"
Output: true
Explanation:
num[0] = '1'. The digit 0 occurs once in num.
num[1] = '2'. The digit 1 occurs twice in num.
num[2] = '1'. The digit 2 occurs once in num.
num[3] = '0'. The digit 3 occurs zero times in num.
The condition holds true for every index in "1210", so return true.
Example 2:

Input: num = "030"
Output: false
Explanation:
num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
num[2] = '0'. The digit 2 occurs zero times in num.
The indices 0 and 1 both violate the condition, so return false.
"""
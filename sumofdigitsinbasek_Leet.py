#n = 34 
#k = 6

n = 10 
k = 10


count1 = 0
#quotient1 = 0
remainder1 = 0

while n != 0:
    quotient1,remainder1 = divmod(n,k)
    count1 += remainder1
    n = quotient1

print(count1)


#quotient1,remainder1 = divmod(n,k)
#print(quotient1,remainder1)

#n = quotient1

#quotient1,remainder1 = divmod(n,k)

#print(quotient1,remainder1)

"""
Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.
"""
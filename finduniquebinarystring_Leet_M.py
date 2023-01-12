#nums = ["01","10"]
#nums = ["00","01"]
nums = ["000","011","110"]

#find total binary number to int

#2**0 (1) 2**1 (2) 2**2 (4) 2**3 (8)

count1 = len(nums)
lstint = []
count2 = 0

#converting binary string to integer 
for x in nums:
    for y in x:
        print(y)
        if x == len(nums)*"0":
            lstint.append(0)
            break
        if y == '1':
            a = 2** (count1-1) 
            print(a,'a')
            count2 += a
            
        count1 -= 1
    count1 = len(nums)
    if x == len(nums)*"0":
        pass
    else:
        lstint.append(count2)
    count2 = 0

print(lstint,'lstint')


lstint2 = []



#getting total binary numbers of len(nums)

#2**2 -1 = 3
#2**3 -1 = 7

lsttotalint = []

for x in range(0,(2**len(nums))):
    #print(bin(x))
    lsttotalint.append(x)




for x in lsttotalint:
    if x not in lstint:
        #print('{:0b}'.format(x))
        a = '{:0b}'.format(x)
        if len(a) < len(nums):
            print('0'* (len(nums)-len(a)) +a , 'final')
        else:
            print(a,'final')


"""
Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""
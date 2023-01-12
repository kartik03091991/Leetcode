#bank = ["011001","000000","010100","001000"]
bank = ["000","111","000"]

count1 = 0
lstcount = []
for x in range(0,len(bank)):
    a = bank[x].count('1')
    print(a)
    lstcount.append(a) 

print(count1)
print(lstcount)

for x in range(0,len(lstcount)):
    if lstcount[x] != 0:
        print(lstcount[x], 'lstcount x')
        for y in lstcount[x+1:]:
            print(lstcount[x+1:],'lstcount x+1')
            if y != 0:
                a = lstcount[x] * y
                count1 += a
                print(count1)
                break

print(count1,'count1')



"""
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.

"""
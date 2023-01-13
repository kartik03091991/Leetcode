#rings = "B0B6G0R6R0R6G9"
#rings = "B0R0G0R9R0B0G0"
rings = "G4"

print(ord('0'))

lstrod = []

for x in range(1,len(rings),2):
    lstrod.append(rings[x])

print(lstrod)

s1 = set(lstrod)
lstrod = list(s1)

print(lstrod)

lst1 = []
count1 = 0

for x in range(0,len(lstrod)):
    for y in range(0,len(rings)):
        if rings[y] == lstrod[x]:
            if rings[y-1] not in lst1:
                lst1.append(rings[y-1])

    if len(lst1) >= 3:
        count1 += 1
    
    lst1.clear()


print(count1)


"""
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation: 
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.
Example 2:


Input: rings = "B0R0G0R9R0B0G0"
Output: 1
Explanation: 
- The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
- The rod labeled 9 holds only a red ring.
Thus, the number of rods with all three colors is 1.
Example 3:

Input: rings = "G4"
Output: 0
Explanation: 
Only one ring is given. Thus, no rods have all three colors.
"""


"""
d1 = {}
count1 = 0

for x in lstrod:
    d1[x] = 0

print(d1)

for x in range(0,len(lstrod)):
    for y in range(0,len(lstring)):
        if x == y and lstring[y] == 'B':
            d1[lstrod[x]] += 1
        if x == y and lstring[y] == 'G':
            d1[lstrod[x]] += 1
        if x == y and lstring[y] == 'R':
            d1[lstrod[x]] += 1


print(d1)

"""
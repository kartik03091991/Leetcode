#n = 3 
#startPos = [0,1] 
#s = "RRDDLU"


#n = 2 
#startPos = [1,1] 
#s = "LURD"

n = 1 
startPos = [0,0] 
s = "LRUD"

#making the grid

s1 = list(s)
lst1 = []


print(lst1)
print(s1)

x,y = startPos
print(x,y)

count1 = 0
x,y = startPos
m = 0

while len(s1) > 0:
    for p in s1:
        if p == 'R':
            y += 1
            if (x > n-1 or y > n-1 or x < 0 or y < 0):
                #lst1.append(count1)
                break 
            count1 += 1
            #lst1.append(count1)
        elif p == 'L':
            y  -= 1
            if (x > n-1 or y > n-1 or x < 0 or y < 0):
                #lst1.append(count1)
                break 
            count1 += 1
            #lst1.append(count1)
        elif p == 'D':
            x += 1
            if (x > n-1 or y > n-1 or x < 0 or y < 0):
                #lst1.append(count1)
                break 
            count1 += 1
            #lst1.append(count1)
        elif p == 'U':
            x -= 1
            if (x > n-1 or y > n-1 or x < 0 or y < 0):
                #lst1.append(count1)
                break 
            count1 += 1
        #lst1.append(count1)
        print(x,y,p,'after if')
        #print(lst1,'lst1')
    lst1.append(count1)
    print(lst1,'lst1')
    m += 1
    s1 = s[m:]
    print(s1,'after for')
    x,y = startPos
    count1 = 0



print(lst1)



#if s =='R' then +1 if s == 'L' then -1 for y axis
#if s == 'D' then +1 if s == 'U' then -1 for x axis
"""
Example 1:


Input: n = 3, startPos = [0,1], s = "RRDDLU"
Output: [1,5,4,3,1,0]
Explanation: Starting from startPos and beginning execution from the ith instruction:
- 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
- 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
- 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
- 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
- 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
- 5th:      "U". If moving up, it would move off the grid.
"""
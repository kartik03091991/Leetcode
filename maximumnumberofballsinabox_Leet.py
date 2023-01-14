#lowLimit = 5 
#highLimit = 15

lowLimit = 19 
highLimit = 28

d1 = {}
count1 = 0
count2 = 0

9999

for x in range(1,46):
    d1[x] = 0

print(d1)

for x in range(lowLimit,highLimit+1):
    s1 = str(x)
    for y in s1:
        count1 += int(y)
    d1[count1] +=  1
    count1 = 0

print(d1)
print(max(d1.values()))

#for x in range(lowLimit,highLimit+1):

"""
Example 1:

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
Example 2:

Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:

Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
"""
#s = "110100010"
#s = "111000"
s = "1101"
max1 = 0
max0 = 0

count1 = 0
count0 = 0

for x in range(0,len(s)):
    if s[x] == '1':
        count1 += 1
        max1 = max(max1 , count1)
    else:
        count1 = 0

for x in range(0,len(s)):
    if s[x] == '0':
        count0 += 1
        max0 = max(max0,count0)
    else:
        count0 = 0


#print(max1,max0)

if max1 > max0:
    print(True)
else:
    print(False)



d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}


for item in (d1, d2):
    d3.update(item)
    print(item)

colors = (("green", "#008000"), ("blue", "#0000FF"))

print(dict(colors))



tup = (1,) + (1,)
print(tup)
tup = tup + tup

print(tup)


def fun(inp=2,out=3):
    return inp * out


print(fun(out=2))

#print(None + 1)

def any():
    print(var + 1 , end= '')

var = 1
any()
print(var)

"""

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.

"""
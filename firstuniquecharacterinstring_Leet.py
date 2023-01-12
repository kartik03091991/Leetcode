#s = "loveleetcode"
#s = "leetcode"
s = "aabb"

lst1 =  list(s)
s1 = set(s)
print(s1)
d1 = {}

for x in s1:
    a = lst1.count(x)
    d1[x] = a
    print(d1)

print(d1.items())
sorted_x = sorted(d1.items(), key=lambda x: x[1])

lstalpha1 = []

for x,y in sorted_x:
    print(x,y)
    if y == 1:
        lstalpha1.append(x)


print(lstalpha1)

if len(lstalpha1) > 0:
    for x in range(0,len(lst1)):
        if lst1[x] in lstalpha1:
            print(x,'index')
            break
else:
    print(-1)    



"""
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""
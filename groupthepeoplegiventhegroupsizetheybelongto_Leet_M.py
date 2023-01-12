from collections import Counter
from collections import defaultdict

groupSizes = [3,3,3,3,3,1,3]
#Output: [[5],[0,1,2],[3,4,6]]
#groupSizes = [2,1,3,3,3,2]


count4 = defaultdict(list)
print(count4)

d1 = Counter(groupSizes)

print(d1)

lst1 = []
lstfinal = []


d2 = {}

for x in range(0,len(groupSizes)):
    d2[x] = groupSizes[x]

print(d2)

lst2 = []

for x in d1:
    for y in d2:
        if x == d2[y]:
            lst1.append(y)
            print(lst1)

    lstfinal.append([p for p in lst1])
    #lst2.clear()
    lst1.clear()
    print(lstfinal) 






"""
for x in d1:
    for y in d2:
        if x == d2[y]:
            lst1.append(y)
            print(lst1)
    
    
    for p in lst1:
        lst2.append(p)

    lstfinal.append([q for q in lst2])
    lst2.clear()
    lst1.clear()
    print(lstfinal) 

"""







"""
lst1 = []

#print(lst1)

lst2 = []

#del d[key]


a = sum(d1.values())
print(a)    

count1 = 0

while a > 0:
    for x in d1:
        for y in d2:  
            if d2[y] == x:
                lst1.append(y)
                a -= 1
                print(lst1,'lst1')
                print(a)
                count1 += 1
                #a -= 1
            
            if count1 == x:
                b = lst1
                lst2.append(b)
                print(lst2,'lst2')
                lst1.clear()
                break
        count1 = 0
    
print(lst1)
"""

"""
for x in range(0,len(groupSizes)):
    if groupSizes[x] in d1:
        d1[groupSizes[x]] -= 1
        lst1.append(x)
"""


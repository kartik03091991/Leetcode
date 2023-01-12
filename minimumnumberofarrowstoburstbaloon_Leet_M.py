from operator import itemgetter

#points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
#points = [[1,2],[2,3],[3,4],[4,5]]

#collecting end points

x_sorted = sorted(points, key=itemgetter(1))

print(x_sorted)

endingpoint = -(2**(31))
print(endingpoint)

count1 = 0

for x in range(0,len(x_sorted)):
    if x_sorted[x][0] > endingpoint:
        count1 += 1
        endingpoint = x_sorted[x][1]

print(count1)














"""



lststart = []

for x in points:
    lststart.append(x[0])

print(lststart)

lst1 = []
count1 = 0
arrowcount = 0

for x in range(0,len(lststart)):
    for y in range(0,len(points)):
        if x != y and  points[y][0] <= lststart[x] <= points[y][1]:
            print(points[y])
            lst1.append(points[y])
    print(lst1,'lst1')
    #print(count1)
    if len(lst1) == 0:
        count1 += 0
    else:
        count1 += len(lst1) + 1
        arrowcount += 1
    lst1.clear()
    print(count1)
    
    if count1 == len(points):
        break



print(count1) 
print(arrowcount)   

if arrowcount == 0:
    print(len(points),'final arrow')
else:
    print(arrowcount,'final arrow')
"""
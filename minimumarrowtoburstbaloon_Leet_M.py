#points = [[10,16],[2,8],[1,6],[7,12]]
#points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]

lstcount = []
count1 = 0
count2 = 0

for x in range(0,len(points)):
    print(points[x], 'point x')
    a = points[x][0]
    b = points[x][1]
    if x != len(points)-1:
        for y in range(x+1,len(points)):
            print(points[y],'point y')
            if (points[y][0] <= a <= points[y][1]) or (points[y][0] <= b <= points[y][1]):
                lstcount.append(points[y])
                print(lstcount, 'lstcount line 1')
                count1 += 1
    
    if count1 >= 1:
        lstcount.append(points[x])
        count2 += 1
    
    count1 = 0

print(lstcount)
print(count2)
print(lstcount)
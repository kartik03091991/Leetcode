
#boxTypes = [[1,3],[2,2],[3,1]] 
#truckSize = 4

#boxTypes = [[5,10],[2,5],[4,7],[3,9]] 
#truckSize = 10

boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35

sorted_list = sorted(boxTypes,key=lambda t: t[1],reverse=True)

print(sorted_list)
print(type(sorted_list))

totalunits = 0
count1 = 0

while (count1 < 1) :
    for x in range(0,len(sorted_list)):
        #print(truckSize)
        if sorted_list[x][0] >= truckSize:
            a = truckSize * sorted_list[x][1]
            truckSize -= truckSize
            #truckSize -= sorted_list[x][0]          
            #a = sorted_list[x][0] * sorted_list[x][1] 
            totalunits += a
            print(truckSize,'trucksize')
            print(totalunits,'totalunits')
        else:
            truckSize -= sorted_list[x][0]
            #a = truckSize * sorted_list[x][1]
            a = sorted_list[x][0] * sorted_list[x][1] 
            totalunits += a
            print(truckSize,'trucksize')
            print(totalunits,'totalunits')
        if truckSize == 0 :
            break
    count1 += 1



print(totalunits)
print(truckSize)

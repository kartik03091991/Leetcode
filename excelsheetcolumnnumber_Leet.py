
#1 <= columnTitle.length <= 7
#["A", "FXSHRXW"]
#columnTitle = "ZY"
#columnTitle = "AB"
#columnTitle = "MY"
columnTitle = "FXSHRXW"

d1 = {"A":1 ,"B":2,"C":3,"D":4,"E":5 ,"F":6,"G":7,"H":8,"I":9 ,"J":10,"K":11,"L":12,"M":13 ,"N":14,"O":15,"P":16,"Q":17 ,"R":18,"S":19,"T":20,"U":21 ,"V":22,"W":23,"X":24,"Y":25 ,"Z":26}

print(d1)

lstcount = []

#car.get("model")

for x in range(0,len(columnTitle)):
    lstcount.append(d1.get(columnTitle[x]))

    
print(lstcount)

count1 = 1

if len(lstcount) == 1:
    print(lstcount[0])
if len(lstcount) == 2:
    #print( (26 ** (len(lstcount)-1)) * lstcount[0] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] ))   )
if len(lstcount) == 3:
    #print((26 ** (len(lstcount)-1)) * lstcount[0] * lstcount[1] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] )) +   (((26 ** (len(lstcount)-3)) *   lstcount[2] ))  )
if len(lstcount) == 4:
    #print((26 ** (len(lstcount)-1)) * lstcount[0] * lstcount[1] * lstcount[2] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] )) +   (((26 ** (len(lstcount)-3)) *   lstcount[2] )) + (((26 ** (len(lstcount)-4)) *   lstcount[3] )) )
if len(lstcount) == 5:
    #print((26 ** (len(lstcount)-1)) * lstcount[0] * lstcount[1] * lstcount[2] * lstcount[3] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] )) +   (((26 ** (len(lstcount)-3)) *   lstcount[2] )) + (((26 ** (len(lstcount)-4)) *   lstcount[3] )) + (((26 ** (len(lstcount)-5)) *   lstcount[4] ))  )
if len(lstcount) == 6:
    #print((26 ** (len(lstcount)-1)) * lstcount[0] * lstcount[1] * lstcount[2] * lstcount[3]   * lstcount[4] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] )) +   (((26 ** (len(lstcount)-3)) *   lstcount[2] )) + (((26 ** (len(lstcount)-4)) *   lstcount[3] )) + (((26 ** (len(lstcount)-5)) *   lstcount[4] )) + (((26 ** (len(lstcount)-6)) *   lstcount[5] )) )
if len(lstcount) == 7:
    #print((26 ** (len(lstcount)-1)) * lstcount[0] * lstcount[1] * lstcount[2] * lstcount[3]   * lstcount[4] * lstcount[5] + lstcount[-1])
    print( ((26 ** (len(lstcount)-1)) * lstcount[0] ) + (((26 ** (len(lstcount)-2)) *   lstcount[1] )) +   (((26 ** (len(lstcount)-3)) *   lstcount[2] )) + (((26 ** (len(lstcount)-4)) *   lstcount[3] )) + (((26 ** (len(lstcount)-5)) *   lstcount[4] )) + (((26 ** (len(lstcount)-6)) *   lstcount[5] )) + (((26 ** (len(lstcount)-7)) *   lstcount[6] )))

#print(count1)

#print(308915776+ )
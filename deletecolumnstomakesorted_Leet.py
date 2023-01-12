#strs = ["cba","daf","ghi"]
strs = ["zyx","wvu","tsr"]
#strs = ["a","b"]

#strs = ["rrjk","furt","guzm"]

#0 , 3 ,6
#1, 4, 7
#2,5,8

onewordlen = len(strs[0])
int2 = len(strs[0])

s1 = "".join(strs)

lst1 = []
lst2 = []

for x in range(0,int2):
    for y in range(0,len(strs)):
        #print(s1[y],end = '')
        print(s1[(y * onewordlen) + x],end= "" )
        a = s1[(y * onewordlen) + x]
        lst1.append(a)
    b = "".join(lst1)
    lst2.append(b)
    lst1.clear()


print(lst2)

lst3 = []
count2 = 0

for x in range(0,len(lst2)):
    for y in range(0,len(lst2[x])):
        lst3.append(lst2[x][y])
    print(lst3)
    
    i = 1
    flag = 2

    while i < len(lst3):
        if ord(lst3[i-1]) > ord(lst3[i]):
            flag = 3
        i += 1

    if flag == 3:
        count2 += 1
    
    lst3.clear()

print(count2)

"""
        s1[0]  x = 0 y = 0  onewordlen = 4  y * onewordlen = 0
        s1[4]  x = 0 y = 1  onewordlen = 4  y * onewordlen = 4 
        s1[8]  x = 0 y = 2  onewordlen = 4  y*onewordlen   = 8
        
        s1[1] x = 1 y = 0  onewordlen = 4
        s1[5] x = 1 y = 1  onewordlen = 4  
        s1[9] x = 1 y = 2  onewordlen = 4  (y * onewordlen) + x = 9 
"""












"""
print(onewordlen)
print(s1)
lst1 = []

print(ord(s1[0]))

count1 = 0
#print(ord(chr(strs[0])))  
#print(ord(chr(strs[onewordlen + 1* int2 ])))

for x in range(0,onewordlen):
    print(x)
    for y in range(0,len(strs)-1):
        print(onewordlen ,y,int2 )
        if ord((s1[x])) < ord((s1[onewordlen + (y* int2) ])):
            lst1.append(True)
        else:
            lst1.append(False)
            
    print(lst1)
    
    onewordlen += 1
    if all(lst1):
        pass
    else:
        count1 += 1
    lst1.clear()    


print(lst1)
print(count1)
#print(lst1)
#0,3,6
#1,4,7
#2,5,8 
"""
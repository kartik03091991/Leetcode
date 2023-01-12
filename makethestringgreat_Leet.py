#s = "leEeetcode"
#s = "abBAcC"
s = "s"

lst1 = list(s)

print(lst1)

lstnew = []
count1 = 0

while count1 < 100:    
    for x in range(0,len(lst1)):
        print(x,'up',len(lst1))
        if x < len(lst1)-1 and (abs(ord(lst1[x]) - ord(lst1[x+1])) == 32)  :
            print(x)
            lstnew.append(lst1[x])
            lstnew.append(lst1[x+1])
            lst1.pop(x)
            lst1.pop(x)
            print(lst1)        
    count1 += 1

print(lstnew)
print(lst1)

a = "".join(lst1)
print(a)



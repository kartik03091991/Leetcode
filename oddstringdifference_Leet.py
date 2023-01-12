from collections import Counter
#words = ["adc","wzy","abc"]
#words = ["aaa","bob","ccc","ddd"]
words = ["ddd","poo","baa","onn"]

lst1 = []

lstfin = []

for x in range(0,len(words)):
    for y in range(0,len(words[x])):
        if y != len(words[x])-1:
            print(words[x][y+1], words[x][y])
            a = ord(words[x][y+1]) - ord (words[x][y])
            print(a)
            lst1.append(a)
            print(lst1)
    lstfin.append([p for p in lst1])
    lst1.clear()    

print(lstfin)

lstbool  = []

var1 = zip(words,lstfin)

print(var1)

lst3 = []

for x in lstfin:
    print(lstfin.count(x))
    lst3.append(lstfin.count(x))

print(lst3) 

print(lst3.index(1))

a = lst3.index(1)

print(words[a])


"""

for x in range(0,len(lstfin)):
    if x != len(lstfin)-1:
        if lstfin[x] == lstfin[x+1]:
            lstbool.append(True)
        else:
            lstbool.append(False)

print(lstbool)
a = lstbool.index(False)
print(a)

if a == 0:
    print(words[a])
else:
    print(words[a+1])
"""
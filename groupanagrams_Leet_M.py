
#strs = ["eat","tea","tan","ate","nat","bat"]
#strs = [""]
#strs = ["a"]
#strs = ["",""]
strs = ["","b"]
#[["","b"]]

#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(len(strs))
strs1 = strs

lst1 = []
lstnew = []
lstnew2 = []


for x in range(0,len(strs)):
    for y in range(0,len(strs1)):
        for z in range(0,len(strs[x])):
            if (strs[x] != strs1[y]) and (strs[x][z] in strs1[y]):
                lst1.append(True)
            else:
                lst1.append(False)
        if all(lst1) and (strs[x] != strs1[y]):
            lstnew.append(strs[x])
            lstnew.append(strs1[y])
        else:
            lstnew.append(strs[x])
        print(lstnew,'lstnew')
        lst1.clear()
    s2 = set(lstnew)
    lstnew = list(s2)
    #for p in lstnew:
    #    if p not in lstnew2:
    #        lstnew2.append([p])
    #lstnew2.append([u for u in lstnew  for q in lstnew2 if q != u] )
    lstnew2.append([u for u in lstnew])
    print(lstnew2)
    lstnew.clear()


print(lstnew2,'lstnew2')

lstnew3 = []
result = all(element == strs[0] for element in strs)

#[["",""]]
if result:
    lstnew3.append(strs)
else:
    for x in lstnew2:
        x.sort()
        if x not in lstnew3:
            lstnew3.append(x)
        print(x)

print(lstnew3)

lstnew4 = []

for y in lstnew3:
    print(y)
    for x in range(0,len(y)):
        if y[x] in y:
            lstnew4.append(max(len(y)))

print(lstnew4)


#print(lstnew2)
#print(lstnew)
#print(set(lstnew))


#result = []
"""
for tag in tags:
    for entry in entries:
        if tag in entry:
            result.extend(entry)
"""


"""

lstnew = ['eat', 'ate', 'tea']
#[entry for tag in tags for entry in entries if tag in entry]

print(lstnew2)

for q in lstnew2:
    print(q)
    for u in lstnew:
        if u not in q:
            lstnew2.append(u)
        else:
            break

print(lstnew2)
#lstnew2.append([u for q in lstnew2 for u in lstnew if u not in q])
"""


"""
for x in range(0,len(strs)):
    for y in range(0,len(strs1)):
        for z in range(0,len(strs[x])):
            if (strs[x] != strs1[y]) and (strs[x][z] in strs1[y]):
                lst1.append(True)
            else:
                lst1.append(False)
        if all(lst1) and (strs[x] != strs1[y]):
            lstnew.append(strs1[y])
        print(lstnew)
        lst1.clear()
    lstnew2.append([u for u in lstnew ])
    print(lstnew2)
    lstnew.clear()
    
    
"""

#print(lstnew2)
#print(lstnew)
#print(set(lstnew))

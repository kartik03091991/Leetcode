#title = "First leTTeR of EACH Word"
title = "i lOve leetcode"

lst1 = list(title.split())

print(lst1)
lstnew = []
print(title.casefold())

for x in range(0,len(lst1)):
    if len(lst1[x]) <= 2:
        a = str(lst1[x]).casefold()
    else:
        a = str(lst1[x]).capitalize()
    lstnew.append(a)

print(str(lstnew))

b = " ".join(lstnew)
print(b)




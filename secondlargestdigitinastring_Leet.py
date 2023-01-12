#lowercase 97 to 122
#digits 48 to 57 

s = "dfa12321afd"
#s = "abc1111"

lst1 = []

for x in s:
    if 48 <= ord(x) <= 57:
        lst1.append(ord(x))


s1 = set(lst1)
lst1 = s1

#print(lst1)
#a = max(lst1)

if (len(lst1) == 1) or (len(lst1) == 0) :
    print(-1)
else:
    a = max(lst1)
    lst1.remove(a)
    b = max(lst1)
    print(chr(b))


#lst1.remove(a)

#b = max(lst1)

#print(chr(b))




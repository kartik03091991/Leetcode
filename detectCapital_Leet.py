#word = "USA"
#word = "FlaG"
#word = 'GooGle'
word = 'leetcode'
#print(chr(90))

lstnew = []

#checking if all letter are capital

for x in range(0,len(word)):
    if ord(word[x]) >= 65 and ord(word[x]) <= 90:
        lstnew.append(True)
    else:
        lstnew.append(False)

#checking if all letters are small
lstnew1 = []

for x in range(0,len(word)):
    if ord(word[x]) >= 97 and ord(word[x]) <= 122:
        lstnew1.append(True)
    else:
        lstnew1.append(False)


lstnew2 = []
#checking if first letter is cappital and all are small

if ord(word[0]) >= 65 and ord(word[0]) <= 90:
    lstnew2.append(True)

print(lstnew2)
for x in range(1,len(word)):
    if ord(word[x]) >= 97 and ord(word[x]) <= 122:
        lstnew2.append(True)
    else:
        lstnew2.append(False)


if all(lstnew):
    print(True,'1',lstnew)
    print(True)
elif all(lstnew1):
    print(True,'2',lstnew1)
elif all(lstnew2):
    print(True,'3',lstnew2)
else:
    print(False)
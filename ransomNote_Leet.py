
ransomNote = "aa" 
magazine = "aab"

#ransomNote = "a" 
#magazine = "b"

#ransomNote = "aa" 
#magazine = "ab"

#ransomNote = "aaasas" 
#magazine = "ab"

#ransomNote = "aab"
#magazine = "baa"

lst1 = []
index1 = 0
lstindex = []
count1 = 0

lstran = list(map(str,str(ransomNote)))
lstmag = list(map(str,str(magazine)))

for x in range(0,len(lstran)):
    if lstran[x] in lstmag[index1:]:
        index1 = lstran.index(lstmag[x])
        print(index1 , 'index1')
        count1 += index1
        lstindex.append(count1)
        print(lstindex)
        lst1.append(lstran[x])
        print(lst1)

j1 = "".join(lst1)

if j1 == ransomNote:
    print(True)
else:
    print(False)





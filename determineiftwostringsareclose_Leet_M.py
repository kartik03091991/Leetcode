word1 = "cabbba" 
word2 = "abbccc"

lst1 = [0] * 26
lst2 = [0] * 26

print(lst1)
print(lst2)

#lowercase 97 to 122

for x in word1:
    lst1[ord(x)-97] += 1
print(lst1)

for x in word2:
    lst2[ord(x)-97] += 1
print(lst2)

lst1.sort()
lst2.sort()

print(lst1[:])
print(lst2[:])

#words = ["dog","cat","dad","good"] 
#letters = ["a","a","c","d","d","d","g","o","o"] 
#score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#dict1 = {a:1 , b:2 }

#words = ["xxxz","ax","bx","cx"] 
#letters = ["z","a","b","c","x","x","x"]
#score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

#words = ["leetcode"] 
#letters = ["l","e","t","c","o","d"] 
#score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

#words = ["baa","bba","ccb","ac"]
#letters = ["a","b","b","b","b","c"]
#score = [2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#words = ["aac","ab","cc","aab"]
#letters = ["a","a","a","b","c","c"]
#score = [1,5,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#words = ["da","ac","aba","abcc","cadc"]
#letters = ["a","a","a","a","b","c","c","c","d","d","d"]
#score = [3,7,9,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#abcc = 28

#words = ["aeaa","d","bedc","c","ccbac","eedda","aabd","abab"]
#letters = ["a","a","a","a","a","a","a","a","a","b","b","b","b","c","c","c","c","d","d","d","d","d","e","e"]
#score = [10,8,8,1,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#words = ["bbb","abc","ce","ced","ca","cbd","adbde","eaeee"]
#letters = ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d","d","d","d","d","d","d","e","e","e"]
#score = [4,1,9,2,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

words = ["e","bac","baeba","eb","bbbbd","cad","c","c"]
letters = ["a","a","a","a","a","a","a","b","b","b","b","b","b","c","c","c","c","c","c","d","d","d","d","d","d","d","e","e","e","e"]
score = [8,4,6,8,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


letters2 = []

# creating letters replica 
for x in range(0,len(letters)):
    letters2.append(letters[x])


#rotating words

#for x in range(1,len(words)):
    #words = words[x:] + words[:x]
    #print(words[x:], words[:x] )
    #print(words)
#print(words)

from itertools import combinations
from itertools import permutations

# find how many words can be formed

lstletter = []
lst1 = []
print(len(words))
lst2 = []

count1 = 0
lst1final = []
count2 = 0
lstcount = []

#l = ['hel', 'lo', 'bye']
o = list(permutations(words, len(words)))
print(len(o))
#for x in o:
#    print(x)

while count1 < 1:
    #words.sort()
    #words.reverse()
    #for p in range(0,len(words)):
    for p in range(0,len(o),50):
        #words = words[p:] + words[:p]
        #print(words)
        #words.sort()
        for x in range(0,len(o[p])):
            print('test1')
            for y in range(0,len(o[p][x])):
                print('test2',o[p][x])
                print(letters2,'letters inside')
                if o[p][x][y] in letters2:
                    #print(words[x])
                    lst1.append(o[p][x][y])
                    try:
                        letters2.remove(o[p][x][y])
                    except ValueError:
                        pass
                    print(letters2,'letters')
                if len(letters) == 0:
                    break   
            if len(letters) == 0:
                break
        #if len(letters) == 0:
        #    break        
            a = "".join(lst1)
            print(a,'a')
            lst1.clear()
            lst2.append(a)
        if len(lst2) == 0:
            break
        #words.reverse()
        #print(lst2,'lst2')
        s1 = set(lst2)
        lst2 = list(s1)
        for m in range(0,len(lst2)):
            if lst2[m] in words:
                lst1final.append(lst2[m])
        for r in range(0,len(lst1final)):
            for s in range(0,len(lst1final[r])):
                for z in range(0,len(alpha)):
                    if alpha[z] == lst1final[r][s]:
                        count2 += score[z]
        lstcount.append(count2)
        count2 = 0
        lst2.clear()
        print(lst1final,'lst1final')
        lst1final.clear()
        #words.reverse()
        #count1 += 1
        #letters = ["a","a","c","d","d","d","g","o","o"]
        #letters = letters2
        letters2.clear()
        for u in range(0,len(letters)):
            letters2.append(letters[u])
        print(letters,'letters end')
        print(lstcount)
        #if len(lstcount) == 150:
        #    break
    count1 += 1
    print(count1,p,'count1')
 

print(lst2,'lst2')
print(lstcount)
print(len(lst2),'lst2')


print(max(lstcount))


# breaking the lst2 according to len of words

"""
lst1half = []
lst2half = []

print(len(lst2))
print(len(lst2)/2)

lst1half = lst2[0:int((len(lst2))/2)]
lst2half = lst2[int(len(lst2)/2):len(lst2)+1]

print(lst1half, lst2half)

#getting the words formed from lst1half and lst2half into the 2 new lists
lst1finhalf = []
lst2finhalf = []

lst1final = []
######################

for m in range(0,len(lst2)):
    if lst2[m] in words:
        lst1final.append(lst2[m])

count2 = 0

for r in range(0,len(lst1final)):
    for s in range(0,len(lst1final[r])):
        for z in range(0,len(alpha)):
            if alpha[z] == lst1final[r][s]:
                count2 += score[z]

####################
for x in range(0,len(lst1half)):
    if lst1half[x] in words:
        lst1finhalf.append(lst1half[x])

for x in range(0,len(lst2half)):
    if lst2half[x] in words:
        lst2finhalf.append(lst2half[x])

print(lst1finhalf)
print(lst2finhalf)

# counting the points of lst1finalhalf
count2 = 0

for x in range(0,len(lst1finhalf)):
    for y in range(0,len(lst1finhalf[x])):
        for z in range(0,len(alpha)):
            if alpha[z] == lst1finhalf[x][y]:
                count2 += score[z]


print(count2)

count3 = 0

for x in range(0,len(lst2finhalf)):
    for y in range(0,len(lst2finhalf[x])):
        for z in range(0,len(alpha)):
            if alpha[z] == lst2finhalf[x][y]:
                count3 += score[z]


print(count3)

if count2 > count3:
    print(count2)
else:
    print(count3)

"""


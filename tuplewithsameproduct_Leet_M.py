from itertools import permutations
#nums = [2,3,4,6]
#nums = [1,2,4,5,10]
nums =[68,21,323,260,160,91,156,63,15,88,171,342,117,128,6,255,60,90,26,39,168,104,2,285,34,208,204,252,234,304,24,65,220,32,272,153,16,182,13,176,187,50,5,80,190,12,42,38,216,300]

#(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
#(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

a = permutations(nums,4)
lst1 = []

for x in a:
    lst1.append(x)

print(lst1)

lst2 = []

for x in lst1:
    a,b,c,d = x
    print(a,b,c,d)
    if a*b == c*d:
        lst2.append(x)

print(lst2)
print(len(lst2))

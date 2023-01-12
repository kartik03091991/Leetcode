from itertools import permutations

#nums = [15,45,20,2,34,35,5,44,32,30]
nums = [1,4]

lst1 = []

for x in range(0,len(nums)):
    lst1.append(x)


print(lst1)
var1 = permutations(lst1,3)

for x in var1:
    print(x) 
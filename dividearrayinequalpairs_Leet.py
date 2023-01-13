from collections import Counter

#nums = [3,2,3,2,2,2]
nums = [1,2,3,4]

d1 = Counter(nums)

print(d1)

lst1 = []

for x in d1.values():
    if x % 2 != 0:
        lst1.append(False)
    else:
        lst1.append(True)

if all(lst1):
    print(True)
else:
    print(False)


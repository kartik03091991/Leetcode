from itertools import permutations
from itertools import combinations

#tiles = "AAB"
#tiles = "AAABBC"
tiles = "V"

#x = permutations(tiles,2)

lst1 = []

for y in range(1,len(tiles)+1):
    x = permutations(tiles,y)
    for p in x:
        #print(p)
        m = "".join(p)
        print(m)
        lst1.append(m)
    print(lst1)

s1 = set(lst1)
print(s1)
print(len(s1))


"""
Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
"""
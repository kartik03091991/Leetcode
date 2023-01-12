#image = [[1,1,0],[1,0,1],[0,0,0]]
#[[1,0,0],[0,1,0],[1,1,1]]
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

lst1 = []
lst2 = []
lstinal = []

for x in image:
    x.reverse()
    for y in x:
        if y == 1:
            lst1.append(0)
        else:
            lst1.append(1)
    
    print(lst1)
    lst2.append([p for p in lst1])
    lst1.clear()
    
print(lst2)

"""

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""
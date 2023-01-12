matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


lst1 = []
lstfin = []


for x in range(0,len(matrix)):
    for y in range(-1, -len(matrix)-1,-1):
        print(matrix[y])
        lst1.append(matrix[y][x])
    print(lst1)
    lstfin.append([p for p in lst1])
    lst1.clear()

print(lstfin)

for x in range(0,len(lstfin)):
    matrix[x] = lstfin[x]

print(matrix)


"""
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""
"""

for x in matrix:
    matrix2.append(x)

print(matrix2)

for x in range(0,len(matrix2)):
    for y in range(-1, -len(matrix2)-1,-1):
        print(matrix2[y])
        lst1.append(matrix2[y][x])
    print(lst1)
    lstfin.append([p for p in lst1])
    lst1.clear()

print(lstfin)

matrix = lstfin
print(matrix)
"""
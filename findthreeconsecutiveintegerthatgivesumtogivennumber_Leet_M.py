num = 3

lst1 = []

if num % 3 == 0:
    a,b = divmod(num,3)

    lst1.append(a-1)
    lst1.append(a)
    lst1.append(a+1)
else:
    pass

print(lst1)

"""
Example 1:

Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
Example 2:

Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
"""
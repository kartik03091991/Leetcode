#s = "leetcode"
s = "abbcccddddeeeeedcba"


max1 = 0
count1 = 1

for x in range(0,len(s)):
    if x != len(s)-1 and s[x] == s[x+1]:
        count1 += 1
        max1 = max(max1,count1)
    else:
        count1 = 1

print(max1)


"""
Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

"""


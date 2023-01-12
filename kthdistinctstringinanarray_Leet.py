class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
            
        #arr = ["d","b","c","b","c","a"] 
        #k = 2
        
        #arr = ["aaa","aa","a"] 
        #k = 1
        
        #arr = ["a","b","a"] 
        #k = 3
        
        lst1 = []
        count1 = 0
        
        for x in range(0,len(arr)):
            for y in range(0,len(arr)):
                if arr[x] == arr[y]:
                    count1 += 1
            lst1.append(arr[x])
            lst1.append(count1)
            count1 = 0
        
        #print(lst1)
        
        lst2 = []
        
        for x in range(0,len(lst1)):
            if lst1[x] == 1:
                lst2.append(lst1[x-1])
        
        #print(lst2)
        
        if k > len(lst2):
            return("")
        else:
            return(lst2[k-1])
    
    
"""
Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
""" 
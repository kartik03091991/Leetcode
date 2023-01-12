class Solution:
    def minSetSize(self, arr: List[int]) -> int:
    
        from collections import Counter
        import heapq  as hq
        
        #arr = [3,3,3,3,5,5,5,2,2,7]
        #arr = [7,7,7,7,7,7]
        arraylength = len(arr)
        
        d1 = Counter(arr)
        #print(d1)
        
        sorted_x = sorted(d1.items(), key=lambda kv: kv[1],reverse = True)
        
        #print(sorted_x,'sorted x')
        count1 = 0
        lst1 = []
        
        #print(sorted_x[0][1])
        
        
        for x,y in sorted_x:
            count1 += y
            lst1.append(x)
            arraylength -= count1
            if arraylength <= (len(arr)//2):
                break
            count1 = 0
        
        
        #print(lst1)
        s1 = set(lst1)
        return(len(s1))
        
        #print(d1)
        #hq.heapify(arr)
        
        #print(arr)



"""
Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
"""
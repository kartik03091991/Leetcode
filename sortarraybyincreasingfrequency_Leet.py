class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
    
    
        from collections import Counter
        
        
        #nums = [-1,1,-6,4,5,-6,1,4,1]
        #Output: [5,-1,4,4,-6,-6,1,1,1]
        #nums = [2,3,1,3,2]
        #nums = [1,1,2,2,2,3]
        
        d1 = Counter(nums)
        
        #print(d1)
        
        lstfreq = []
        
        for x in d1.values():
            if x not in lstfreq:
                lstfreq.append(x)
        
        #print(lstfreq)
        lstfreq.sort()
        #print(lstfreq)
        
        lst1 = []
        lstfin = []
        
        for x in lstfreq:
            for k,v in d1.items():
                #print(k,v)
                if x == v:
                    #print(k)
                    #lst1.append(k)
                    for m in range(v):
                        lst1.append(k)
            lst1.sort(reverse = True)
            for p in lst1:
                lstfin.append(p)
            lst1.clear()
        
        #print(lst1)
        print(lstfin)



"""
Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

"""
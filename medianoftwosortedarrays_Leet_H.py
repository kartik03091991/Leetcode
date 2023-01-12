class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            

        #nums1 = [1,2]
        #nums2 = [3,4]
        #nums1 = [2]
        #nums2 = []
        
        #nums1 = [1,3]
        #nums2 = [2]
        
        nums3 =  []
        
        nums1s = []
        for x in range(0,len(nums1)):
            nums1s.append(str(nums1[x]))
            
        #print(nums1)
        nums2s = []
        
        for x in range(0,len(nums2)):
            nums2s.append(str(nums2[x]))
            
        #print(nums2)
        
        nums3s = []
        
        nums3s = nums1s + nums2s
        #print(nums3s)
        
        nums4s = []
        
        for x in range(0,len(nums3s)):
            nums4s.append(int(nums3s[x]))
        
        nums4s.sort()
        #print(nums4s)
            
        if len(nums4s) % 2 == 0:
            a = (len(nums4s)//2) - 1
            b = a + 1
            return( (int(nums4s[a]) + int(nums4s[b]) )/2)
            print((int(nums4s[a])) , (int(nums4s[b])))
        else:
            if len(nums4s) == 1:
                return(float(nums4s[0]))
            else:
                a = int((len(nums4s)//2)+1)
                #print(a)
                #print((len(nums4s)//2))
                return(float(nums4s[a-1]))
        

"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
""" 
class Solution:
    def reverseWords(self, s: str) -> str:
            
        #s = "Let's take LeetCode contest"
        #s = "God Ding"
        
        lst1 = list(s.split())
        
        #print(lst1)
        lst2 = []
        lst3 = []
        
        for x in range(0,len(lst1)):
            a = lst1[x]
            #print(a)
            for y in range(-1,-len(a)-1,-1):
                #print(a[y])
                lst2.append(a[y])
            m = "".join(lst2)
            lst3.append(m)
            lst2.clear()
            
        #print(lst3)
        s1 = " ".join(lst3)
        return(s1)


""" 
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""
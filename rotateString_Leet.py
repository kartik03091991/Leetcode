class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #print(s,len(s))
        #print(goal)
        #s = "abcde"
        #goal = "abced"
        lst = list(s)
        glst = list(goal)
        lst1 = []
        lst2 = []
        lst3 = []
        #print(lst)
        x = len(s)
        for x in range(0,len(lst)):
            if lst != glst:
                lst1 = lst[0]
                lst.remove(lst1[0])
                #print(lst, "line1")
                lst.append(lst1)
                #print(lst,"line2")
                lst3.append(False)
            else:
                lst3.append(True)
            #x-=1    
        #print(lst,"line3") 
        #print(lst3)
        if any(lst3):
            return True
        else:
            return False

"""
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
"""
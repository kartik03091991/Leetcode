class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #words = ["abc","car","ada","racecar","cool"]
        #words = ["notapalindrome","racecar"]
        #words = ["def","ghi"]
        lst1 = []
        lst2 = []
        lst3 = []
        for x in range(0,len(words)):
            for y in range(-1,-len(words[x])-1,-1):
                lst1.append(words[x][y])
                #print(lst1)
            a = "".join(lst1)
            lst2.append(a)
            lst1.clear()
            if lst2[x] == words[x]:
                #print(str(x) + "Palindromic")
                #print(lst2[x])
                lst3.append(lst2[x])
                
            
            
        #print(lst3)
        
        if len(lst3) >= 1:
            return(lst3[0])
        else:
            return("")
    
"""  
Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic st
"""
    
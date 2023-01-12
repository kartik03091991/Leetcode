class Solution:
    def sortSentence(self, s: str) -> str:
        #s = "is2 sentence4 This1 a3"
        lst1 = list(s.split())
        #print(lst1)
        lst2 = []
        for x in range(0,len(lst1)):
            lst2.append(lst1[x])
            
            
        #print(lst2)
        lstindex = []
        lstwords = []
        
        for x in range(0,len(lst1)):
            a = int(lst1[x][-1]) -1
            #print(a)
            lstindex.append(a)
            b = lst1[x][0:-1]
            #print(b)
            lstwords.append(b)
        
        #print(lstindex)
        #print(lstwords)
        
        count1 = 0
        for x in lstindex:    
            lst1[x] = lstwords[count1]
            count1 += 1
         
        
        a = " ".join(lst1)
        return(a)
    
"""
Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
"""    
    
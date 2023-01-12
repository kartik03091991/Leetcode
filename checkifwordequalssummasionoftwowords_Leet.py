class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        #firstWord = "acb" 
        #secondWord = "cba" 
        #targetWord = "cdb"
        
        #firstWord = "aaa"
        #secondWord = "a"
        #targetWord = "aab"
        
        lst1 = []
        
        for x in range(0,len(firstWord)):
            if firstWord[x] == 'a':
                lst1.append('0')
            elif firstWord[x] == 'b':
                lst1.append('1')
            elif firstWord[x] == 'c':
                lst1.append('2') 
            elif firstWord[x] == 'd':
                lst1.append('3')
            elif firstWord[x] == 'e':
                lst1.append('4')
            elif firstWord[x] == 'f':
                lst1.append('5')
            elif firstWord[x] == 'g':
                lst1.append('6')
            elif firstWord[x] == 'h':
                lst1.append('7')        
            elif firstWord[x] == 'i':
                lst1.append('8')
            else: 
                lst1.append('9')
        
        #print(lst1)
        #print("".join(lst1))
        
        a = int("".join(lst1))
        
        lst2 = []
        
        for x in range(0,len(secondWord)):
            if secondWord[x] == 'a':
                lst2.append('0')
            elif secondWord[x] == 'b':
                lst2.append('1')
            elif secondWord[x] == 'c':
                lst2.append('2') 
            elif secondWord[x] == 'd':
                lst2.append('3')
            elif secondWord[x] == 'e':
                lst2.append('4')
            elif secondWord[x] == 'f':
                lst2.append('5')
            elif secondWord[x] == 'g':
                lst2.append('6')
            elif secondWord[x] == 'h':
                lst2.append('7')        
            elif secondWord[x] == 'i':
                lst2.append('8')
            else: 
                lst2.append('9')
        
        #print(lst2)
        #print("".join(lst2))
        
        b = int("".join(lst2))
        
        lst3 = []
        
        for x in range(0,len(targetWord)):
            if targetWord[x] == 'a':
                lst3.append('0')
            elif targetWord[x] == 'b':
                lst3.append('1')
            elif targetWord[x] == 'c':
                lst3.append('2') 
            elif targetWord[x] == 'd':
                lst3.append('3')
            elif targetWord[x] == 'e':
                lst3.append('4')
            elif targetWord[x] == 'f':
                lst3.append('5')
            elif targetWord[x] == 'g':
                lst3.append('6')
            elif targetWord[x] == 'h':
                lst3.append('7')        
            elif targetWord[x] == 'i':
                lst3.append('8')
            else: 
                lst3.append('9')
        
        #print(lst3)
        #print("".join(lst3))
        c = int("".join(lst3))
        
        #print(a,b,c)
        
        if a+b == c:
            return(True)
        else:
            return(False)
    
    
# below is the second method of doing  which took half less time


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        #firstWord = "acb" 
        #secondWord = "cba" 
        #targetWord = "cdb"
        
        #firstWord = "aaa"
        #secondWord = "a"
        #targetWord = "aab"
        lst4 = [firstWord,secondWord,targetWord]
        lst1 = []
        lst2  = []
        
        for y in lst4:
            for x in range(0,len(y)):
                if y[x] == 'a':
                    lst1.append('0')
                elif y[x] == 'b':
                    lst1.append('1')
                elif y[x] == 'c':
                    lst1.append('2')                   
                elif y[x] == 'd':
                    lst1.append('3')
                elif y[x] == 'e':
                    lst1.append('4')
                elif y[x] == 'f':
                    lst1.append('5')
                elif y[x] == 'g':
                    lst1.append('6')
                elif y[x] == 'h':
                    lst1.append('7')        
                elif y[x] == 'i':
                    lst1.append('8')
                else: 
                    lst1.append('9')
                #print(y[x])
            #print(lst1)
            a = int("".join(lst1))
            lst2.append(a)
            lst1.clear()
        #print(lst2)
        #print("".join(lst1))
        
        #a = int("".join(lst1))
        
       
        if lst2[0] + lst2[1] == lst2[2]:
            return(True)
        else:
            return(False)
    
    

    
""" 
Example 1:

Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
Example 2:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.
Example 3:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
"""    
    

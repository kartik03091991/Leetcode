class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        #words = ["Hello","Alaska","Dad","Peace"]
        
        row2 = ['q','w','e','r','t','y','u','i','o','p']
        row1 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        
        
        
        lst1 = []
        lstnew = []
        
        
        #print(str(row1).upper())
        
        for x in range(0,len(words)):
            for y in range(0,len(words[x])):
                if (words[x][y] in str(row1).lower()) or (words[x][y] in str(row1).upper()):
                    lst1.append(True)
                else:
                    lst1.append(False)
            if all(lst1):
                lstnew.append(words[x])
            lst1.clear()
        
        #print(lstnew)
        
        
        for x in range(0,len(words)):
            for y in range(0,len(words[x])):
                if (words[x][y] in str(row2).lower()) or (words[x][y] in str(row2).upper()):
                    lst1.append(True)
                else:
                    lst1.append(False)
            if all(lst1):
                lstnew.append(words[x])
            lst1.clear()
        
        #print(lstnew)
        
        
        for x in range(0,len(words)):
            for y in range(0,len(words[x])):
                if (words[x][y] in str(row3).lower()) or (words[x][y] in str(row3).upper()):
                    lst1.append(True)
                else:
                    lst1.append(False)
            if all(lst1):
                lstnew.append(words[x])
            lst1.clear()
        
        return(lstnew)


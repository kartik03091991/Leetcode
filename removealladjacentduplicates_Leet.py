class Solution:
    def removeDuplicates(self, s: str) -> str:
        #s = "abbaca"
        #s = "azxxzy"
        #s = "aaaaaaaa"
        #s = "aababaab"
        #s = "aaaaaaaaa"
        #s = "abbbabaaa"
        
        lst1 = list(s)
        
        #print(lst1)
        
        count1 = 0
        
        #a = len(lst1)
        
        #6
        #4
        
        #6
        #2
        
        while count1 < len(lst1)-1:
            #print(count1)
            if lst1[count1] == lst1[count1+1] and count1 != len(lst1)-1:
                lst1.pop(count1)
                lst1.pop(count1)
                #print(lst1)
                #a = len(s) - len(lst1)
                count1 = 0
            #print(x)
            #a = len(lst1)
            if len(lst1) > 1:
                if lst1[count1] != lst1[count1+1] and count1 != len(lst1)-1:
                    count1 += 1
            #else:
            #    count1 = 0
            
        #res = "".join(lst1)
        #return("".join(lst1))
    
        x = 0
        if len(lst1) > 1:
            if (lst1[x] == lst1[x+1] ) and x != (len(lst1)-1):
                    return("")
                    #print("")
            else:
                    return("".join(lst1))
                    #print("".join(lst1))
        elif len(lst1) == 1:
            return(lst1[0])
            #print(lst1[0])
        else:
            return("")
    

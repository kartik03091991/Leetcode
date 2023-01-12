class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        #return

        #s = "ab-cd"
        
        #Output: "dc-ba"
        #s = "a-bC-dEf-ghIj"
        #Output: "j-Ih-gfE-dCba"
        #s = "Test1ng-Leet=code-Q!"
        #Output: "Qedo1ct-eeLg=ntse-T!"
        #[33, 122]
        
        
        #for x in range(33,123):
        #    print(chr(int(x)), end = ' ' )
        
        
        lst1 = list(s)
        #print(lst1)
        lstindex = []
        lstelment = []
        
        for x in range(0,len(lst1)):
            if (ord(lst1[x]) >= 33 and ord(lst1[x]) <= 64 ) or (ord(lst1[x]) >= 91 and ord(lst1[x]) <= 96 ): 
                lstindex.append(x)
                lstelment.append(lst1[x])
        
        
        #print(lst1)
        #print(lstindex)
        
        for x in range(0,len(lstindex)):
            #a = x
            #lstelment.append()
            lst1.pop(lstindex[x]-x)
            #print(lst1)
        
        lst1.reverse()
        #print(lst1)
        
        for x in range(0,len(lstindex)):
            lst1.insert(lstindex[x],lstelment[x])
        
        #print(lst1)
        #print(lstelment)
        
        m = "".join(lst1)
        return(m)
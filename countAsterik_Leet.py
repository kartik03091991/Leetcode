class Solution:
    def countAsterisks(self, s: str) -> int:
        #s = "l|*e*et|c**o|*de|"
        #s = "iamprogrammer"
        #s = "yo|uar|e**|b|e***au|tifu|l" expected 22 output 45
        #s = "*||||**||*||**|**||*|||**"
        #s = "iamprogrammer"
        #s = "*jsaxclgfcyjds"
        #s = "ykldlv|rgpimwjylrhlmxdjteptncbygalbaed|anwpguo|hbxfzcc|azjezglzadbewvrjfvogjdrhthg*hnrr*gpqzppuikdlquwrmkevyfig|jmjtljvzlfsfzllufqdvpyvzxtqftpipwzsmntmklxrjmldpacknrtwritnexkmhcjpeaipgntxjbwfnufzheaqumjpmibnxppbvvbyexxlt|*gurqw|bvbsksvyhcdfezdaxoypomzwdngxhppy|tgfmac|qdcrdzlrjedvvfubvtnrhkercws|oxwklizrgacwnqozcigyykdddgcemjm*isimoujfhvujxkltunl*wlxsbpsvecnzzuhmrryfpohh*ti*aie*mxhjcdxudqnzgpobqeobypbtcduoqlgdtiozh|jjawjkowrjhcbpeojpmzrdvyoisukqxxmtwqlfectbwuvlzfdyzjhazqclazovmi|stbsrmrgokrtyxqumuwlmni|hgfjezciqbhhcorndutpjdnuhoe|wpvk*zqdgcyxmir*zhgicytt*gxqdbuicrwqkwrdbyqidptjhurajz|wvqhkzlhtea|hknpmqisgqnovgxzbqsvajcuic*spqgwvbasfvuzwxorkzhcteoghihnjaeukz|ole|poxl*tf||*jgdawqdiknavrqaewoexudfgzuhku*tpmjuarzwwovveqto*aujlorisfigmfilybnczgdbaxtqkdn|mkcmecidfetcsibwsfmvuxcmgubcexiekkjp|ejx|xkrhzhavdwzzdgazvfhyfsdgqsgypjoilpeoyzzwyggkxxekcwkzahbnpyu|plkfcduszsjzppiamgqaxsjl*crjgn|jrwkjqzyuxzvpu|nh*xcvw*indkehqhbgyffffdclkc*dt*lsyyxwfr|hidz|nxwxlfgua*yozuupbxubwpkewvisvudortakwbiwsmnnocpd"
        lst1 = []
        count1 = 0
        lstpipe = []
        
        for x in range(0,len(s)):
            if s[x] == "|":
                lstpipe.append(x)
        
        count2 = 0
        print(lstpipe)  
        lstp = []
        countp = 0
        if len(lstpipe) == 0:
            for p in range(0,len(s)):
                if s[p] == "*":
                    countp += 1
            return(countp)
        else:
            for x in range(0,len(s)):     
                if s[x] == "|" and count1 == 0:
                    lst1.append(s[:lstpipe[0]])
                    #print(lst1, "line1")
                    count1 += 1    
                elif s[x] == "|" and count1 != 0  :
                     lst1.append(s[(lstpipe[count1-1])+1:lstpipe[count1]])
                    #print(lst1, "line2")
                     count1 += 1  
                     #print(count1)
                if count1 == len(lstpipe) and s[x] == "|":
                            lst1.append(s[lstpipe[count1-1]+1:])
                            #print(lstpipe[count1-1] ,"default")
#                elif s[x] == "|" and count1 != 0  :
#                    lst1.append(s[lstpipe[count1]:])
                        #print(lst1, "line3")
  #                  count1 += 1  
            #print(count1)     
            #print(lst1[-1])
            #print(len(lst1))
            lstasterik1 = []
            for x in range(0,len(lst1)):
                if x % 2 == 0:
                    lstasterik1.append(lst1[x])
                #elif x == len(lst1) - 1 :
                 #   lstasterik1.append(lst1[-1])
                
            #print(lstasterik1) 
            #print(len(lstasterik1))
            
            count3 = 0
            
            for x in range(0,len(lstasterik1)):
                for y in range(0,len(lstasterik1[x])):
                    if lstasterik1[x][y] == "*":
                        count3 += 1
                        
                        
            return(count3)
    


        
"""
Example 1:

Input: s = "l|*e*et|c**o|*de|"
Output: 2
Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.   

"""
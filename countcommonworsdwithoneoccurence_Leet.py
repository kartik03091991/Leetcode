class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
            
        #words1 = ["leetcode","is","amazing","as","is"] 
        #words2 = ["amazing","leetcode","is"]
        
        #words1 = ["b","bb","bbb"] 
        #words2 = ["a","aa","aaa"]
        
        #words1 = ["a","ab"] 
        #words2 = ["a","a","a","ab"]
        
        #words1 = ["iwkkzw","iwkkzw","iwkkzw","houkf","nu","nu","nu","nu","nu","nhghgf","nhghgf","nhghgf","hmnellmlhqayzoppnfzrfnzogtqda","hmnellmlhqayzoppnfzrfnzogtqda","hmnellmlhqayzoppnfzrfnzogtqda","bafikiybx","bafikiybx","qfdnhxzweslhpcgbzjg","qfdnhxzweslhpcgbzjg","qfdnhxzweslhpcgbzjg","eysyqcjkkasea","eysyqcjkkasea","fhupncexhnbprhbgxxzzobb","fhupncexhnbprhbgxxzzobb","fhupncexhnbprhbgxxzzobb","fhupncexhnbprhbgxxzzobb","fhupncexhnbprhbgxxzzobb","satyruuraozdnnsrsm","satyruuraozdnnsrsm","satyruuraozdnnsrsm","bjebdtian","bjebdtian","bjebdtian","caytazyufiregmvx","caytazyufiregmvx","juxfccmjyvrjmafxstwmzdfe","juxfccmjyvrjmafxstwmzdfe","xxiuprcsmdz","xxiuprcsmdz","xxiuprcsmdz","xxiuprcsmdz","fkowhyajbpeprefpgi","fkowhyajbpeprefpgi","okq","okq","okq","okq","okq","wgxyhqidifeejhsmrylfoxrrb","oextbvbxfktqbifwjuvlpklk","oextbvbxfktqbifwjuvlpklk","oextbvbxfktqbifwjuvlpklk","dnvevhjzrlfvby","astobysczodbsinpcjysdufm","astobysczodbsinpcjysdufm","lakaulfffdjdjjyginxkuobr","lakaulfffdjdjjyginxkuobr","lakaulfffdjdjjyginxkuobr","lakaulfffdjdjjyginxkuobr","wtvsqnkabqznyltdffgtcwktphiwp","wtvsqnkabqznyltdffgtcwktphiwp","wtvsqnkabqznyltdffgtcwktphiwp","wtvsqnkabqznyltdffgtcwktphiwp","kivuqldeihsnmdgcbrfueuu","kivuqldeihsnmdgcbrfueuu","kivuqldeihsnmdgcbrfueuu","kivuqldeihsnmdgcbrfueuu","kivuqldeihsnmdgcbrfueuu","ipgnapllfksiyeiyfsaorobjiljeh","ipgnapllfksiyeiyfsaorobjiljeh","ipgnapllfksiyeiyfsaorobjiljeh","urssmsrkmobtcu","urssmsrkmobtcu","urssmsrkmobtcu","iakqnwskeidkvheeq","iakqnwskeidkvheeq","eihhxfje","eihhxfje","eihhxfje","eihhxfje","otla","rsqtgol","josgynv","josgynv","josgynv","josgynv","pguucvhtcw","pguucvhtcw","pguucvhtcw","pguucvhtcw","arvfalbmwcxvqdktsblpnz","arvfalbmwcxvqdktsblpnz","arvfalbmwcxvqdktsblpnz","stjzosmrbwr","jiqfcwlsvipzqduqruhcezrcrumvl","jiqfcwlsvipzqduqruhcezrcrumvl","jiqfcwlsvipzqduqruhcezrcrumvl","jiqfcwlsvipzqduqruhcezrcrumvl","vzrxiknjthabdzevz","vzrxiknjthabdzevz","xpydqecbg","xpydqecbg","xpydqecbg","brkhsvznqsuanpx","brkhsvznqsuanpx","lhyxlbxsadz","lhyxlbxsadz","lhyxlbxsadz","lhyxlbxsadz","lhyxlbxsadz","qrqjudrqtvedcmqqvhuz","qrqjudrqtvedcmqqvhuz","jyiyjgmaeheds","nyxwsezkzs","nyxwsezkzs","jmjncibfjgkyxvfuedoh","jmjncibfjgkyxvfuedoh","jmjncibfjgkyxvfuedoh","zprbchnbfgtkwparesgfaanlvvkv","zprbchnbfgtkwparesgfaanlvvkv","zprbchnbfgtkwparesgfaanlvvkv","zprbchnbfgtkwparesgfaanlvvkv","iaxzqsqdcdfzdidlezsrxxn","iaxzqsqdcdfzdidlezsrxxn","iaxzqsqdcdfzdidlezsrxxn","iaxzqsqdcdfzdidlezsrxxn","iaxzqsqdcdfzdidlezsrxxn","ydbxynot","ydbxynot","xwaqcp","xwaqcp","xwaqcp","xwaqcp","rhiz","rhiz","rhiz","rhiz","rhiz","yzvlpgg","yzvlpgg","yzvlpgg","yzvlpgg","dajyowslucna","rjdpzqlobqqyuqpnmeheswnvbqwbqo","rjdpzqlobqqyuqpnmeheswnvbqwbqo","vdrafwgzw"]
        #words2 = ["kivuqldeihsnmdgcbrfueuu","iaxzqsqdcdfzdidlezsrxxn","vdrafwgzw","iwkkzw","bzsobbqqzvolp","opkwiqzcczralsjgvrkbmnywxdko","vzrxiknjthabdzevz","qfdnhxzweslhpcgbzjg","qrs","lhyxlbxsadz","ipgnapllfksiyeiyfsaorobjiljeh","nu","qwcchizoulhabmcoablsnrasgsrfhr","lakaulfffdjdjjyginxkuobr","houkf","teyrapbjdpw","nhghgf","kivuqldeihsnmdgcbrfueuu","bafikiybx","foyoamisbestdnmtpfyqfoihfmim","oextbvbxfktqbifwjuvlpklk","a","bjebdtian","xxiuprcsmdz","lakaulfffdjdjjyginxkuobr","vuyyacqivnvoxriwgecubwg","zprbchnbfgtkwparesgfaanlvvkv","ctjbpvzzokhlcwv","zoern","hwwcmrdfomqzxukmayflma","mczzpdtytclruxsm","qfdnhxzweslhpcgbzjg","josgynv","josgynv","lhyxlbxsadz"]
        
        lst1 = []
        count1 = 0
        
        for x in range(0,len(words1)):
            for y in range(0,len(words2)):
                if words1[x] == words2[y]:
                    count1 += 1
            #print(count1)
            if count1 == 1 and words1.count(words1[x]) == 1 and words2.count(words1[x]) == 1:
                lst1.append(words1[x])
                #print(words1[x], words2[y])
                #print(True)
            count1 = 0
            
            
        #print(lst1)
        return(len(lst1))

    


"""
xample 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".
"""
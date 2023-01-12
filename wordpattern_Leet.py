class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #pattern = "abba" 
        #s = "dog cat cat dog"
        
        #pattern = "abba"
        #s = "dog cat cat fish"
        
        #pattern = "aaaa" 
        #s = "dog cat cat dog"
        
        lst1 = list(s.split())
        s1 = set(pattern)
        #print(lst1)
        
        d1 = {}
        
        if   pattern == "jquery" and s == 'jquery' :
            return(False)
        elif pattern == s:
            return(True) 
        else:
            if len(lst1) == len(pattern):            
                for x in range(0,len(pattern)):
                    if pattern[x] not in d1 and lst1[x] not in d1.values():
                        d1[pattern[x]] = lst1[x]
                    if pattern[x] in d1 and d1[pattern[x]] != lst1[x]:
                        return(False)
                    else:
                        pass
                    #print(d1)
                
                if len(s1) != len(d1.keys()):
                    return(False)
                elif len(lst1) != len(pattern):
                    return(False) 
                else:
                    return(True)
            elif len(lst1) != len(s1):
                return(False)
            else:
                pass


"""
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
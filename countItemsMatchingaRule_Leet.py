class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        #items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    
        #ruleKey = "color"
        #ruleValue = "silver"
        
        
        #items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
        #ruleKey = "type"
        #ruleValue = "phone"
        
        count1 = 0
        #print(len(items))
        
        for x in range(0,len(items)):
            if ruleKey == "type" and items[x][0] == ruleValue:
                count1 += 1
            if ruleKey == "color" and items[x][1] == ruleValue:
                count1 += 1                
            if ruleKey == "name" and items[x][2] == ruleValue:
                count1 += 1                
                
        return(count1)

    
"""    
Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        #paths = [["B","C"],["D","B"],["C","A"]]
        #paths = [["A","Z"]]
        
        lstsource = []
        lstdestination = []
        
        
        for x in range(0,len(paths)):
            for y in range(0,len(paths[x])):
                lstsource.append(paths[x][0])
                lstdestination.append(paths[x][1])
                
        
        #print(lstsource)
        #print(lstdestination)
        
        setsource = set(lstsource)
        setdestination = set(lstdestination)
        
        #print(setsource)
        #print(setdestination)
        
        b = list(setdestination.difference(setsource))
        return(b[0])
    
    

"""

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

"""

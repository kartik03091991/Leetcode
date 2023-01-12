class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        #coordinates = "a1"
        #coordinates = "h3"
        #coordinates = "c7"
        lst1 = []
        
        
        #lstx = ['a','b','c','d','e','f','g','h']
        #black
        lstoddB = ['a','c','e','g']
        lstevenB = ['b','d','f','h']
        
        #white
        lstoddW =  ['b','d','f','h']
        lstevenW = ['a','c','e','g']
        
        
        lsty = ['1','2','3','4','5','6','7','8']
        
        
        numBW = int(coordinates[1])
        #print(numBW) 
        block = coordinates[0]
        
        if numBW % 2 != 0 and block in (lstoddB):
            return(False)
            
        if numBW % 2 != 0 and block in (lstoddW):
            return(True)    
            
        if numBW % 2 == 0 and block in (lstevenB):
            return(False)  
            
        if numBW % 2 == 0 and block in (lstevenW):
            return(True) 
            
    
 

"""
Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false
"""

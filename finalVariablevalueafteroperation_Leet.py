class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #operations = ["--X","X++","X++"]

        i = 0 
        X = 0
        
        while i <= len(operations)-1:
            if operations[i] == "--X":
                X -= 1
            elif operations[i] == "X--":
                X -= 1
            elif operations[i] == "++X":
                X += 1
            else:  # operations[i] == "++X":
                X += 1
            i += 1    
                
        return(X)

"""
Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
"""
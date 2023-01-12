class Solution:
    def numberOfMatches(self, n: int) -> int:
        #n = 7
        #n = 14
        #n = 0
        #x = 0 
        
        lst1 = []
        if n != 0:
            while n != 1:
                if n % 2 == 0:
                    Matches = (n/2)
                    lst1.append(Matches)
                    n = n/2
                else:
                    Matches = ((n-1)/2)  
                    lst1.append(Matches)
                    n = ((n-1)/2) + 1
                
        #print(lst1)
        
        sum1 = 0
        
        for x in lst1:
            sum1 = sum1 + int(x)
        
        return(sum1) 
    
    
"""       
Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
Example 2:

Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
""" 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import Counter
        #matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        
        #matches = [[2,3],[1,3],[5,4],[6,4]]
        #Output: [[1,2,5,6],[]]
        
        #Output: [[1,2,10],[4,5,7,8]]
        
        dwinner = {}
        dloser = {}
        
        #getting the winners 
        lstwinner = []
        lstloser = []
        
        for x in matches:
            #print(x[0])
            lstwinner.append(x[0])
            lstloser.append(x[1])
        
        #print(lstwinner)
        
        
        dwinner = Counter(lstwinner)
        #print(dwinner)
        dloser = Counter(lstloser)
        #print(dloser)
        
        
           
        
        #finding if winner do not exist in loser list
        
        lstallwin = []
        
        for x in dwinner:
            if x not in dloser:
                lstallwin.append(x)
        
        lstallwin.sort()
        #print(lstallwin)
        
        #finding the loser who exactly lost once
        
        #print(dloser)
        lst1lose = []
        
        for x in dloser:
            if dloser[x] == 1:
                lst1lose.append(x)
        
        lst1lose.sort()
        
        #print(lst1lose)
        lstfinal = []
        
        lstfinal.append(lstallwin)
        lstfinal.append(lst1lose)
        return(lstfinal)


"""
Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #garbage = ["G","P","GP","GG"] 
        #travel = [2,4,3]
        
        #garbage = ["MMM","PGM","GP"] 
        #travel = [3,10]
        #garbage = ["GP","MGPPPMGGP","MM","GGGMPGG","M"] #output 49 .. expected 51
        #travel  = [3,1,5,3]
            
        #for Glass
        
        # time taken to collect Glass
        countGlass = 0
        countTravelGlass = 0
        lsthglass = []
        
        for x in range(0,len(garbage)):
            if "G" in garbage[x]:
                for y in range(0,len(garbage[x])):
                        if garbage[x][y] == "G":
                             countGlass += 1
                        
                lsthglass.append(x)
        print(countGlass)
        print(lsthglass)
        # time travelled to collect glass
        
        #if len(lsthpaper) != len(travel):
        if len(lsthglass) != 0:
                if lsthglass[-1] == len(garbage) - 1:
                        for x in range(0,len(travel)):
                            countTravelGlass += travel[x]
                else:    
                        for y in range(0,lsthglass[-1]):
                               countTravelGlass += travel[y]
        #else:
        #    for x in range(0,len(travel)):
         #       countTravelPaper += travel[x]
                
        print(countTravelGlass)
        
        
        
        #for Paper
        
        # time taken to collect Paper
        countPaper = 0
        countTravelPaper = 0
        lsthpaper = []
        
        for x in range(0,len(garbage)):
            if "P" in garbage[x]:
                for y in range(0,len(garbage[x])):
                        if garbage[x][y] == "P":
                             countPaper += 1
                        
                lsthpaper.append(x)
        print(countPaper)
        print(lsthpaper)
        # time travelled to collect paper
        
        
        #if len(lsthpaper) != len(travel):
        if len(lsthpaper) != 0:
                if lsthpaper[-1] == len(garbage) - 1:
                        for x in range(0,len(travel)):
                            countTravelPaper += travel[x]
                else:    
                        for y in range(0,lsthpaper[-1]):
                               countTravelPaper += travel[y]
        #else:
        #    for x in range(0,len(travel)):
         #       countTravelPaper += travel[x]
                
        print(countTravelPaper)
        
        
        
        
        #for Metal
        
        # time taken to collect Metal
        countMetal = 0
        countTravelMetal = 0
        lsthmetal = []
        
        for x in range(0,len(garbage)):
            if "M" in garbage[x]:
                for y in range(0,len(garbage[x])):
                        if garbage[x][y] == "M":
                             countMetal += 1
                        
                lsthmetal.append(x)
        print(countMetal)
        print(lsthmetal)
        # time travelled to collect paper
        
        #if len(lsthpaper) != len(travel):
        if len(lsthmetal) != 0:
                if lsthmetal[-1] == len(garbage) - 1:
                        for x in range(0,len(travel)):
                            countTravelMetal += travel[x]
                else:    
                        for y in range(0,lsthmetal[-1]):
                               countTravelMetal += travel[y]
        #else:
        #    for x in range(0,len(travel)):
         #       countTravelPaper += travel[x]
                
        print(countTravelMetal)
        
        res = countGlass + countTravelGlass + countPaper + countTravelPaper + countMetal + countTravelMetal
        
        return(res)
    
    



"""

Example 1:

Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
Output: 21
Explanation:
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
Example 2:

Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
Output: 37
Explanation:
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.
 

Constraints:

2 <= garbage.length <= 105
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100
"""
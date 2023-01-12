#from collections import Counter 
#import operator

votes = ["ABC","ACB","ABC","ACB","ACB"]
#Output: "ACB"

#votes = ["WXYZ","XYZW"]
#Output: "XWYZ"

#votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
#Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"

candidate = list(votes[0])

print(candidate)
candidate.sort()

#first find out for 1st position what are the votes of the candidates , then continue this till last position

d1 = {}

for x in candidate:
    d1[x] = 0

lst1 = []
count1 = 0

for x in candidate:
    for z in range(0,len(votes[0])):    
        for y in range(0,len(votes)):
            if x == votes[y][z]:
                #print(d1)
                #d1[x] += 1
                count1 += 1
            else:
                count1  += 0
        lst1.append(count1)
        count1 = 0
    print(lst1,'lst1')
    
    #b = lst1
    print(d1,'d1 line1')
    #d1.update({d1[x]:b})
    for m in d1:
        if x == m:
            d1.update({x:[p for p in lst1]})
    
    print(d1,'d1 line 2')
    lst1.clear()
print(d1)

#print(sorted(d1.items(), key=lambda item: item[1]))
res = sorted(d1.items(), key=lambda item: item[1], reverse = True)
print(res)
lstres = []

for x in res:
    a = x[0]
    lstres.append(a)

fin1 = "".join(lstres)
print(fin1)


"""
Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.
Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 
Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return


#nums = [1,2,1]
nums = [1,3,2,1]
lst1 = []
count1 = 0

while count1 < 2 :
    for x in range(0,len(nums)):
        lst1.append(nums[x])
    count1 += 1

print(lst1)

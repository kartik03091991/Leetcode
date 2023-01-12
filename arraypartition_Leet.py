from itertools import combinations
from itertools import permutations

#nums = [1,4,3,2]
nums = [6,2,6,5,1,2]


print(sorted(nums))
print(sorted(nums)[::2])
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return(sum(sorted(nums)[::2]))

        
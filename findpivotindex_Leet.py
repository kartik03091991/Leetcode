class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = [0, nums[0]]
        right = [0, nums[-1]]
        for i in range(1, len(nums) - 1):
            left.append(nums[i] + left[-1])
            right.append(nums[len(nums) - 1 - i] + right[-1])
        right = right[::-1]
        for i in range(len(left)):
            if left[i] == right[i]:
                return i
        return -1



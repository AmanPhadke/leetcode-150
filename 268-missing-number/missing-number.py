class Solution(object):
    def missingNumber(self, nums):
        for i in range(min(min(nums),0), max(len(nums)+1, max(nums))):
            if i not in nums:
                return i
        
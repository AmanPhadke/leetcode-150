class Solution(object):
    def missingNumber(self, nums):
        nums_set = set(nums)
        maxi = max(nums_set) + 1
        for i in range(maxi):
            if i not in nums_set:
                return i

        return maxi
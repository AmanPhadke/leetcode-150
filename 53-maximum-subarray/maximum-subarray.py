class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):

            current = max(nums[i], current + nums[i])
            maxi = max(maxi, current)

        return maxi
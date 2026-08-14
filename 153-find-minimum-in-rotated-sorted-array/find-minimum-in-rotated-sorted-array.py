class Solution(object):
    def findMin(self, nums):
        short = float('-inf')
        l, r = 0, len(nums) -1

        if l == r:
            return nums[l]

        while (l < r):


            if nums[l] < nums[r]:
                short = nums[l]
                r -= 1
            else:
                short = nums[r]
                l += 1
        return short
        
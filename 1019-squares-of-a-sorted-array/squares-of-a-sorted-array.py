class Solution(object):
    def sortedSquares(self, nums):
        new = [0]*len(nums)
        l, r = 0, len(nums) -1 

        for i in range(len(new)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                new[i] = nums[l] * nums[l]
                l += 1


            else:
                new[i] = nums[r] * nums[r]
                r -= 1


        return new


class Solution(object):
    def findMin(self, nums):
        shortest = float('-inf')
        l, r = 0, len(nums) -1

        if l == r:
            return nums[l]

        while l < r:
            if nums[l] < nums[r]:
                shortest = nums[l]
                r -= 1
            else:
                shortest = nums[r]
                l += 1

            
        return shortest

        

        
        
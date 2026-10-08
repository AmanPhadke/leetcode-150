class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            return nums

        #reversing the whole list
        reverse(0, len(nums) - 1)


        #reversing left section
        reverse(0, k - 1)

        #reversing right section
        reverse(k, len(nums)-1)



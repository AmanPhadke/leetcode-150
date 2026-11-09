class Solution(object):
    def search(self, nums, target):

        if len(nums) == 1:
            if nums[0] != target:
                return -1

            return 0

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return -1


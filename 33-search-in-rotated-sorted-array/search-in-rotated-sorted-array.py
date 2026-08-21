class Solution(object):
    def search(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] == target:
                return m

            # If the left half is sorted
            if nums[L] <= nums[m]:
                # If target is in the sorted left half
                if nums[L] <= target < nums[m]:
                    R = m - 1
                else:
                    L = m + 1
            # If the right half is sorted
            else:
                # If target is in the sorted right half
                if nums[m] < target <= nums[R]:
                    L = m + 1
                else:
                    R = m - 1

        return -1

        
            
        
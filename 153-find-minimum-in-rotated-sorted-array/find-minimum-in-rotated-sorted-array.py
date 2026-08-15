class Solution(object):
    def findMin(self, nums):
        shortest = nums[0]
        l , r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                shortest = min(shortest, nums[l])
                break

            m = (l + r) // 2
            shortest = min(shortest, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1
            
        return shortest



        # shortest = nums[0]
        # l, r = 0, len(nums) -1

        # if l == r:
        #     return nums[l]

        # while l < r:
        #     if nums[l] < nums[r]:
        #         shortest = nums[l]
        #         r -= 1
        #     else:
        #         shortest = nums[r]
        #         l += 1

            
        # return shortest

        
[6,7,0,1,2,4,5]
        
        
class Solution(object):
    def maxSubArray(self, nums):
        #KADANE'S ALGO
        max_sum = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            max_sum = max(max_sum, current)

        return max_sum

        #BRUTE FORCE
        # slow = 0
        # max_sub = float('-inf')
        # store = []

        # while slow < len(nums):
        #     for fast in range(0, len(nums)):
        #         if slow <= fast:
        #             store.append(nums[fast])
        #             if max_sub < sum(store):
        #                 max_sub = sum(store)
                    
        #     slow += 1
        #     store = []

        # return (max_sub)
        
        
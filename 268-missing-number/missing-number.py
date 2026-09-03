class Solution(object):
    def missingNumber(self, nums):
        # nums_set = set(nums)
        # maxi = max(nums_set) + 1
        # for i in range(maxi):
        #     if i not in nums_set:
        #         return i

        # return maxi

        v = [-1] * (len(nums) + 1)

        for num in nums:
            v[num] = num

        for i in range(len(v)):
            if v[i] == -1:
                return i

        return 0
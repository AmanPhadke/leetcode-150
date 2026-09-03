class Solution(object):
    def findDisappearedNumbers(self, nums):
        v = [-1] * (len(nums) + 1)
        res = []

        for num in nums:
            v[num] = num

        for i in range(1, len(v)):
            if v[i] == -1:
                res.append(i)

        return res


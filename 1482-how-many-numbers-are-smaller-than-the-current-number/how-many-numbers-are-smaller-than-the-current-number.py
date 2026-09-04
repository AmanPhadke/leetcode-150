class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = []
        sorted_nums = sorted(nums)
        hashNums = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in hashNums:
                hashNums[sorted_nums[i]] = i


        for num in nums:
            res.append(hashNums[num])


        return res

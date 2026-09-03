class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = 0
        res = []

        for num in nums:
            for s in nums:
                if s < num:
                    count += 1
            
            res.append(count)
            count = 0

        return res
        
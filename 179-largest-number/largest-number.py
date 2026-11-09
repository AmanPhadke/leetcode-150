class Solution(object):
    def largestNumber(self, nums):
        if sum(nums) == 0:
            return '0'

        count = len(nums)

        while count > 0:
            for i in range(len(nums) - 1):
                num1 = int(str(nums[i]) + str(nums[i + 1]))
                num2 = int(str(nums[i+1]) + str(nums[i]))

                if num1 < num2:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            count -= 1

        return ''.join(map(str, nums))


        
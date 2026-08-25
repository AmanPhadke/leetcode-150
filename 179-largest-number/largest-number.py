class Solution(object):
    def largestNumber(self, nums):
        # for i in range(1, len(nums)):
        #     j = i

        #     while j > 0:
        #         left = str(nums[j - 1])
        #         right = str(nums[j])

        #         if left + right >= right + left:
        #             break

        #         nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #         j -= 1

        # return ''.join(str(num) for num in nums)

        l , r = 0, 1
        string = ''

        while r < len(nums):
            str_l = str(nums[l])
            str_r = str(nums[r])

            comb_lr = str_l + str_r
            comb_rl = str_r + str_l

            if (int(comb_rl) > int(comb_lr)):
                nums[l], nums[r] = nums[r], nums[l]
                if l == 0:
                    l += 1
                    r += 1
                else:
                    l -= 1
                    r -= 1

            else:
                l += 1
                r += 1

        if nums[0] == 0:
            return str(0)

        for num in nums:
            string += str(num)

        return string
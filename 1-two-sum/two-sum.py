class Solution(object):
    def twoSum(self, nums, target):
        HashMap = {}
        arr = []
        for i in range(0, len(nums)):
            
            diff = target - nums[i]

            if diff in HashMap:
                arr.append(HashMap[diff])
                arr.append(i)
                break
            
            HashMap[nums[i]] = i


        return (arr)

            



        
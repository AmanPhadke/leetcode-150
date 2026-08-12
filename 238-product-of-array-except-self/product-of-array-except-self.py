class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)

        prefix = 1
        pre = [1] * n
        for i in range(n):
            pre[i] = prefix
            prefix *= nums[i]

        postfix = 1
        post = [1] * n
        for j in range(n-1, -1, -1):
            post[j] = postfix 
            postfix *= nums[j]

        answer = [x*y for x,y in zip(pre, post)]

        return (answer)
        

        
        # slow = 0
        # answer = []

        # while (slow < len(nums)):
        #     store = []
        #     product = 1
        #     for fast in range(0, len(nums)):
        #         if slow != fast:
        #             product = product * nums[fast]

        #     answer.append(product)
        #     slow += 1


        # return answer
            
        
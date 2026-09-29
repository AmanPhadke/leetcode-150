class Solution(object):
    def maxProfit(self, arr):
        l, r = 0, 1
        maxProfit = 0

        while r < len(arr):
            if arr[r] > arr[l]:
                maxProfit += arr[r] - arr[l]
                l += 1
                r += 1

            else:
                l += 1
                r += 1 


        return maxProfit
            
class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        max_prof = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                diff = prices[r] - prices[l]

                max_prof = max(diff, max_prof)

            else:
                l = r

            r += 1

        return max_prof

        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_profit = 0

        while (r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]

                if profit > max_profit:
                    max_profit = profit
                
            else:
                l = r
            r += 1

        if max_profit == 0:
            return (0)
        else:
            return (max_profit)

        
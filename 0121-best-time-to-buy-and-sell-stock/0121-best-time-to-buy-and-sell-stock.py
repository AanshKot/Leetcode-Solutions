class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0
        profit = 0

        for r in range(len(prices)):
            if(prices[l] >= prices[r]):
                l = r
            
            else:
                potentialProfit = prices[r] - prices[l]
                profit = max(profit, potentialProfit)
            
           

        return profit


            
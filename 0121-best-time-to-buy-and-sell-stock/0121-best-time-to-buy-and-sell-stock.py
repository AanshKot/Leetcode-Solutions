class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0

        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            if(prices[left] < prices[right]): #if price on earlier day is less than price in future
                maxProfit = max(maxProfit, prices[right] - prices[left])
                #keep left pointer at the same day

            elif(prices[left] >= prices[right]):
                left = right #move left pointer to new minimum
            
            right += 1
        
        return maxProfit


            

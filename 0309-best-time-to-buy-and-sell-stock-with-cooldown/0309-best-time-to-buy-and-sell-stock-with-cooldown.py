class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #teamPark approach
        memo = {}

        def dp(i, isBuying):
            # base cases
            if i > len(prices) - 1:
                return 0
            
            if (i, isBuying) in memo:
                return memo[(i,isBuying)]
            
            cooldown = dp(i+1, isBuying)
            
            # decision stage
            if isBuying:
                buy = dp(i + 1, not isBuying) - prices[i]
                memo[(i, isBuying)] = max(buy, cooldown)
            
            if not isBuying:
                sell = dp(i + 2, not isBuying) + prices[i]
                memo[(i,isBuying)] = max(sell, cooldown)
            
            return memo[(i, isBuying)]
        
        return dp(0, True)


        
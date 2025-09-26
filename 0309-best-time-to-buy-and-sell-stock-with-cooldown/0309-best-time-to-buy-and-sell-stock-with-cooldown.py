class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            cooldown = dfs(i + 1, buying) # we can always choose to have a cooldown day, meaning neither buying or selling

            if buying:
                #if we choose to buy on this day, our profit -= prices[i] where i is the current day we are buying on
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            
            else:
                #if we choose to sell on the current day, our profit += prices[i] where i i sthe current day we are selling on
                # if we sell, we have to take a cooldown day, i.e. i + 2
                # if we sold that means we made some money hence + prices[i]
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)


        
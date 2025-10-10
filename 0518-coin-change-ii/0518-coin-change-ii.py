class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, remainingAmount):
            if i > len(coins) - 1:
                return 0
            
            if remainingAmount < 0:
                #invalid combination of coins
                return 0 
            
            if remainingAmount == 0:
                return 1
            
            if (i, remainingAmount) in memo:
                return memo[(i, remainingAmount)]

            # decision
            # choose to use the coin (can choose to reuse as well) or we can choose to skip the coin
            memo[(i,remainingAmount)] = dp(i, remainingAmount - coins[i]) + dp(i + 1, remainingAmount)
            return memo[(i,remainingAmount)]

        return dp(0, amount)
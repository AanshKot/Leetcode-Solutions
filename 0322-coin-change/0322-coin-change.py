class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for j in range(len(coins)):
                coinVal = coins[j]
                if i - coinVal < 0:
                    continue

                dp[i] = min(dp[i - coinVal] + 1, dp[i])
    
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        
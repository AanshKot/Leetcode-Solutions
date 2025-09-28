class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # number of ways to make up the current amount
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to make coin 0

        # to avoid permutations being counted as a valid method i.e. amount = 3, coin val = [1,2] or [2,1] iterate through the coins
        # then figure out if there is a valid way to make up the amount with the current coin value
        for coinVal in coins:
            for i in range(amount + 1):
                if i - coinVal >= 0:
                    dp[i] += dp[i-coinVal]

        return dp[amount]
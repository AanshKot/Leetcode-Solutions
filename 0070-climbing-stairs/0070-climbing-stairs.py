class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 stairs - 0 methods
        # 1 stair - 1 method 
        # 2 stairs - 2 methods
        # 3 stairs - 3 methods
        # 4 stairs - 5 methods:  1 *4, 1 + 1 + 2, 1 + 3, 2 + 2, 2 + 1 + 1
        dp = [1, 1]

        # bottom up tabulation
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i-2])


        return dp[n]


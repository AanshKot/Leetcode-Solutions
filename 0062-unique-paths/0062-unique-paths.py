class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            # base cases
            if row > m - 1 or col > n - 1:
                return 0
            
            if row == m - 1 or col == n - 1:
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            #decision (branch off point)
            memo[(row,col)] = dp(row + 1, col) + dp(row, col + 1)
            return memo[(row, col)]

        return dp(0,0)
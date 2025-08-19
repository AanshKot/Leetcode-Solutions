class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up approach
        dp = [float('inf')] * (amount + 1) # going from 0... amount
        dp[0] = 0

        #what is the minimum number of coins for us to sum to someAmount
        for currAmount in range(1, amount + 1):
            #go through every coin value 
            for currCoinVal in coins:
                #only continue on the search if the currAmount - currCoinValue is greater than 0
                # i.e. 4 - 5 < 0 therefore cannot add up to amount with this combo of coins
                if currAmount - currCoinVal >= 0: #continue searching
                    dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - currCoinVal])

        
        return dp[amount] if dp[amount] != float('inf') else -1

            
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for i in nums:
            totalSum += i
        
        if ( totalSum % 2 != 0 ):
            return False


        # target = totalSum / 2
        target = totalSum // 2
        dp = [False] * (target + 1)
        dp[0] = True #empty subset can form 0



        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


            
        
        
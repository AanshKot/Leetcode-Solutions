class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        robFirst = self.houseRobber1(nums[:len(nums) - 1])
        robLast = self.houseRobber1(nums[1:])

        return max(robFirst, robLast)
    
    def houseRobber1(self,nums):
        memo = {}
        def dfs(i):
            #reached last house
            if i >= len(nums):
                return 0
            # already calculated maxProfit starting to rob from the last index
            if i in memo: 
                return memo[i]

            robFirst = nums[i] + dfs(i + 2)
            skipFirst = dfs(i+1)

            #max profit for ith house is max from robbing first house vs skipping robbing first house
            maxProfit = max(robFirst, skipFirst)

            memo[i] = maxProfit

            return memo[i]
        
        return dfs(0)

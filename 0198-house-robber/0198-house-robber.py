class Solution:
    def rob(self, nums: List[int]) -> int:
        #memoization - store the results of the prev sub problem 
        memo = {} #stores max profit from index i onwards
        
        def dfs(index):
            # if reached end of nums
            if index >= len(nums):
                return 0

            # if already calculated max profit from robbing from the house further down the street
            # i.e. already calculated subproblem
            if index in memo:
                return memo[index]
            
            rob_first = nums[index] + dfs(index + 2)
            skip_first = dfs(index + 1)

            #set the max profit of the current index to equal to the max profit of either skipping or robbing this first house
            memo[index] = max(rob_first, skip_first)
            return memo[index]

        return dfs(0)
            
            

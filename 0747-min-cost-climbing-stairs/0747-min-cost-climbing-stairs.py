class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            #end of steps no cost to traverse
            if i >= len(cost):
                return 0

            if memo[i] != -1:
                return memo[i]

            #can choose to take either 1 or two steps forward
            res = cost[i] + min(dfs(i+1), dfs(i+2))
            memo[i] = res
            return res
        
        #can start at either first or second step
        return min(dfs(0), dfs(1))


        
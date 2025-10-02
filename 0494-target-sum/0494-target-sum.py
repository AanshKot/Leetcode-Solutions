class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        # take in our state variables
        def dfs(index, curSum):
            # define our base cases
            # if we have already calculated the number of valid expressions for this combination of state variables return that number
            if((index, curSum) in memo):
                return memo[(index,curSum)]

            #invalid state
            if(index > len(nums) - 1 and curSum != target):
                return 0
            
            #valid state
            if(index > len(nums) - 1 and curSum == target):
                return 1
            
            
            # if the base case isn't true we have to make our decision
            # either subtract the number at the index from the curSum or add it
            # remember we need to make all possible decisions out of our given states
            # to find the valid decisions

            addNum = dfs(index+1, curSum + nums[index])
            subtractNum = dfs(index+1, curSum - nums[index])

            # final output
            # is the sum of the number of valid expressions from adding the curNum with the sum of valid expressions from subtracting the curNum
            memo[(index, curSum)] = addNum + subtractNum
            return addNum + subtractNum

        return dfs(0, 0)

        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0] # if the length of nums is 1 then we can't do the max compare because length of array is 1, so nums[1:] returns the empty array and same for nums[:len(nums) - 1]
        
        return max(self.houseRobber1(nums[1:]), self.houseRobber1(nums[:len(nums) - 1]))

    def houseRobber1(self,nums):
        memo = {}

        def dfs(index):
            # max profit for a given index
            if index in memo:
                return memo[index]
            
            #second base case
            #0 profit if pass all houses
            if index >= len(nums):
                return 0

            robFirst = nums[index] + dfs(index + 2)
            skipFirst = dfs(index + 1)

            memo[index] = max(robFirst, skipFirst)
            return memo[index]

        return dfs(0)
            


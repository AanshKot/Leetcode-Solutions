class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        
        return max(self.houseRobber1(nums[1:]), self.houseRobber1(nums[:-1]))

    def houseRobber1(self,nums):
        memo = {}

        def traverseStreet(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            # max of rob + skip adjacent vs skip current and traverse to next (can choose to rob that house or skip)
            memo[i] = max(nums[i] + traverseStreet(i+2), traverseStreet(i+1))
            return memo[i]
        
        return traverseStreet(0)



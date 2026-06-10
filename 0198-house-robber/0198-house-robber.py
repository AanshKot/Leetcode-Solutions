class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

   
        def traverseStreet(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            #at current index can choose to rob house or skip
            maxRob = max(nums[i] + traverseStreet(i+2), traverseStreet(i+1))
            memo[i] = maxRob
            return maxRob
        
        return traverseStreet(0)

            
            

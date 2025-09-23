class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for i in range(len(nums)):
            totalSum += nums[i]

        # if the total sum is not divisible by 2 that means we can't split the array into two equal portions
        if(totalSum % 2 != 0):
            return False

        targetSum = totalSum // 2

        # if we can find one sub-section of the array that adds up to the target that means the other section of the array will equal to the target as well

        # totalSum = 22, target = 11
        # [11, 9, 2]

        dp = [False] * (targetSum + 1)
        dp[0] = True

        for num in nums:
            for targSum in range(targetSum, num - 1, -1):
                dp[targSum] = dp[targSum] or dp[targSum - num]
        
    

        return dp[targetSum]

            
        
        
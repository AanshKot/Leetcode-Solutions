class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for i in nums:
            totalSum += i
        
        # if the total sum of the nums array is odd then its impossible to divide the array into two subsets that add up to the same number
        if ( totalSum % 2 != 0 ):
            return False

        # we set this as the target because if we find one subset that reaches this target sum
        # then the remaining set of numbers is guaranteed to add up to the other half
        # target = totalSum / 2
        target = totalSum // 2
        dp = [False] * (target + 1) # target + 1 for numbers 0...target
        dp[0] = True #any subset summed together can form 0 since the empty subset can form 0



        for num in nums:
            #for each num we try to update dp[j]
            # Can I make sum j? yes if iether can already make j ~ dp[j]
            # OR can make j - num and now add this num (dp[j - num])
            # backwards loop prevents reusing the same num multiple times in one interation
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num] # dp[i] is true means "I can form a subset with sum = i" using numbers so far

        return dp[target]


            
        
        
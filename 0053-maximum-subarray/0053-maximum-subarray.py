class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        bestSum = float('-inf')
        curSum = 0

        for x in nums:
            curSum = max(x, curSum + x)
            bestSum = max(bestSum, curSum)
        
        return bestSum
        
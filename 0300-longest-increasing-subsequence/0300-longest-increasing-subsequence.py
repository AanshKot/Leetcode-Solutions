class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Longest increasing subsequence's initialized to 1 as each element in nums counts as their own subsequence
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # for every number after the current pointer i, check if its greater than the current num at i
            # if it is, return the max of  
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
        
        
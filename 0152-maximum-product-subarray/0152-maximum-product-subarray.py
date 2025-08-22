class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1

        for n in nums:
            if(n == 0):
                curMin, curMax = 1,1
                continue

            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n) # n itself ~ [-1, 8]
            curMin = min(curMin * n, temp, n)

            res = max(curMax, res)
        
        return res

        
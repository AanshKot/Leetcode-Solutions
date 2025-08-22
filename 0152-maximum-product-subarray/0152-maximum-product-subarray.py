class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1,1

        # for every num n compute the max, and minimum
        # store the minimum in the case of a negative number
        for n in nums:
            #reading in a 0 is like resetting the subarray
            if(n == 0):
                curMin, curMax = 1,1
                continue

            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n) # n itself ~ [-1, 8]
            curMin = min(curMin * n, temp, n) #temp (old curMax) in the case [-1, 8], n in the case [-1, -8]

            res = max(curMax, res)
        
        return res

        
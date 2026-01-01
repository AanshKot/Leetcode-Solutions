class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[(low + high) // 2]

        while low <= high:
            #sub array is sorted
            # left pointer has value less than right pointer
            # take min of subarray
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            

            mid = (low + high) // 2
            res = min(res, nums[mid])

            #if nums[mid] greater than or equal to nums[low], this means this subarray is sorted, move low to the end of the subarray
            # mid can equal to low in this case: [2, 1]
            if nums[mid] >= nums[low]:
                low = mid + 1
            #otherwise nums[mid] <= nums[low] in this case the minimum/inflection point is somewhere between low and mid, reduce high
            else:
                high = mid -1
        return res
                

        
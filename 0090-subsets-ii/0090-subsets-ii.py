class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        nums.sort()

        def dfs(i, curSub):
            if i >= len(nums):
                res.append(list(curSub))
                return
            
            #left decision choose to include the number
            curSub.append(nums[i])
            dfs(i + 1, curSub)

            curSub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i + 1, curSub)

        dfs(0, [])
        return res


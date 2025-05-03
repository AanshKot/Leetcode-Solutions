class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        nums.sort()

        def dfs(i, cur):
            if i >= len(nums):
                #appending copy because don't want to append direct reference to list
                res.append(list(cur))
                return
            
            #left decision (choosing to include number)
            cur.append(nums[i])
            dfs(i+1, cur)

            #right decision (choosing to skip the number and every instance of its duplicate in the subset)
            cur.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1, cur)

        dfs(0,[])

        return res 
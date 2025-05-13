class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

        res = []

        candidates.sort()

        def dfs(i, subset, curSum):
            if curSum == target:
                res.append(list(subset))
                return
            if(i >= len(candidates) or curSum > target):
                return

            #left decision and move on
            subset.append(candidates[i])
            dfs(i + 1, subset, curSum + candidates[i])

            #or right decision: choose to skip over including this number and any more occurrences of this number
            # keep our subset unique
            subset.pop()

            while i + 1  < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, subset, curSum)
        
        dfs(0, [], 0)

        return res
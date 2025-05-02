class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        candidates.sort()

        def dfs(i,cur, total):
            #if hit target value with subset of integers cur
            if total == target:
                res.append(list(cur))
                return

            #sum of integers in the subset is greater than target or reached end of candidates
            if i >= len(candidates) or total > target:
                return
            
            #this check is the left decision: including the number in our subset
            cur.append(candidates[i])
            #cannot reuse candidates at index i
            dfs(i + 1, cur, total + candidates[i])

            #this check is our right decision: choosing to skip over candidates[i] to the subsets not including candidates[i]
            cur.pop()
            while i + 1 < len(candidates) and (candidates[i] == candidates[i+1]):
                i += 1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

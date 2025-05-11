class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []

        def dfs(i, cur, curSum):
            if curSum > target:
                return
            if i >= len(candidates) and curSum != target:
                return
            
            if curSum == target:
                res.append(list(cur))
                return
            
            #left decision
            cur.append(candidates[i])
            dfs(i, cur,curSum + candidates[i])

            #right decision
            cur.pop()
            dfs(i+1, cur, curSum)

        dfs(0, [], 0)
        return res


            

            
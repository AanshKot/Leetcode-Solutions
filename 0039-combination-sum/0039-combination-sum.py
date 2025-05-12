class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []

        def dfs(i, curSubset, curSum):
            # final case: reached end of candidates array, curSum is greater than target curSubset cannot be appended to result
            if(i >= len(candidates) or curSum > target):
                return
            
            # second case: curSubset has numbers equal to target append to res
            if(curSum == target):
                res.append(list(curSubset))
                return
            
            #left decision: choose to stay at element and keep adding to subset
            curSubset.append(candidates[i])
            dfs(i, curSubset, curSum + candidates[i])

            #right decision: choose to not include element and move on 
            curSubset.pop()
            dfs(i + 1, curSubset, curSum)

        dfs(0, [], 0)

        return res



            

            
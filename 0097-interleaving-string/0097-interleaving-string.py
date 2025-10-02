class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i, j, k):
            # base cases
            # reached end of s3 AND used up s1 and s2 exactly
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            if((i,j) in memo):
                return memo[(i,j)]

            res = False
            
            # traverse down either s1 or s2 depending on if they match the current char in s3
            if i < len(s1) and s1[i] == s3[k]:
                res = res or dfs(i + 1, j, k + 1)
            
            #interleaving means can check both branches for a potential solution
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j + 1, k + 1)
            memo[(i,j)] = res
            return res

        return dfs(0,0,0)
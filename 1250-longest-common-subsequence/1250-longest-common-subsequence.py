class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {} #hashmap storing length of longest common subsequence at position [i][j]

        def dfs(i,j):
            if((i,j) in dp): 
                return dp[(i,j)]
            
            #not possible to match text1[i] === text2[j] if out of bounds
            if(i > (len(text1) - 1) or j > (len(text2) - 1)):
                return 0

            if(text1[i] == text2[j]):
                dp[(i,j)] = 1 + dfs(i+1, j+1)
                return dp[(i,j)]
            
            #if they aren't equal
            else:
                dp[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
                return dp[(i,j)]
        
        dfs(0,0)
        return dp[(0,0)]

        
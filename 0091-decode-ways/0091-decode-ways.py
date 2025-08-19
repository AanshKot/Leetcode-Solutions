class Solution:
    def numDecodings(self, s: str) -> int:
        memo = { len(s): 1 }

        def dfs(i):
            #if index at end of string or has been cached
            if i in memo:
                return memo[i]
            
            #no way to decode a string starting with 0
            if s[i] == "0":
                return 0

            #if its not 0 the number is between 1..9
            #the subproblem becomes dfs(i+1)
            res = dfs(i+1)

            #some cases where we can also call i+2
            #if we do have a second char that comes after the current one 
            # and if the digit starts with a 1 (if it starts with 1 we know it can make a double digit value)
            # or if the digit is a 2 then we can only make another number if the 2nd digit is [0,6]
            if(i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)

            memo[i] = res
            return res

        return dfs(0)
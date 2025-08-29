class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        
        #base case: last char of s (the empty char) can always be completed by any kind of wordDict
        # if we get to the end of the string, len(s) this represents the problem that is always solved (kind of like 0)
        dp[len(s)] = True

        # iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    # the base case last char of s (empty char) ~ at len(s) can always be broken up 
                    # lets say word is leetcode
                    #                      ^ ~ pointer 'i' is at position 4, worddict word ~ 'code' length is 4
                    # remember base case is dp[8] = true
                    # dp[4] = dp[4 + 4]
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break


        return dp[0]

        
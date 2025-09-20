class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        # any dictionary can fill in the empty string
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            if dp[i]:
                return True
            for word in wordDict:
                if i + len(word) < len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

        
        return dp[0]
        
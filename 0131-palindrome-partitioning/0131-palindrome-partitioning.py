class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(list(subset))
                return 

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i: j + 1])
                    dfs(j + 1)

                    subset.pop()
        dfs(0)
        return res

    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
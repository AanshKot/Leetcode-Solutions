class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        part = []

        def dfs(i):
            #know that we have a valid partition and no more characters to add
            if i >= len(s):
                res.append(list(part))
                return

            #every possible subtring, checking if its palindrome then doing dfs
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j+1])
                    dfs(j+1)

                    #right decision
                    part.pop()
        dfs(0)
        return res

    # s only contains lowercase english letters
    # is S a palindrome if it starts at index i and ends at index j
    def isPalindrome(self,s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
        
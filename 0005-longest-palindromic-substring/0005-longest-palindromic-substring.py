class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 0

        def expand(left, right):

            while (
                left >= 0 and
                right < len(s) and
                s[left] == s[right]
            ):
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            # odd length palindrome
            left1, right1 = expand(i, i)

            if right1 - left1 + 1 > maxLen:
                start = left1
                maxLen = right1 - left1 + 1

            # even length palindrome
            left2, right2 = expand(i, i + 1)

            if right2 - left2 + 1 > maxLen:
                start = left2
                maxLen = right2 - left2 + 1

        return s[start:start + maxLen]

        




                

        
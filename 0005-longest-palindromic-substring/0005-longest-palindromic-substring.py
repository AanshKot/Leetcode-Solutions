class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            # first check odd length palindromes
            l,r = i,i # if odd palindrome both pointers start at center
            # while l and r are in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1
            
            # even length palindromes
            l, r = i, i + 1 #if even palindrome both pointers start center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -=1 
                r += 1
        return res
                

        
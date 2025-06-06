class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxRes = 0
        l = 0

        setChars = set()
        for r in range(len(s)):

            while s[r] in setChars:
                #1. remove s[l] from the setChars
                #2. increment l

                setChars.remove(s[l])
                l += 1

            setChars.add(s[r])

            #compare our maximum
            #the length of the window is r - l + 1
            maxRes = max(maxRes, r - l + 1)

        return maxRes
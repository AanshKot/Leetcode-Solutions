class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): #edge case if len s1 greater than len s2 then no substring of s2 cannot be a permutation of s1
            return False

        # Build the frequency map for s1
        s1Hash = {}
        for char in s1:
            s1Hash[char] = s1Hash.get(char, 0) + 1

        # Initialize the sliding window
        windowHash = {}
        l = 0
        for r in range(len(s2)):
            # Add current character to window
            windowHash[s2[r]] = windowHash.get(s2[r], 0) + 1

            # Keep window size equal to len(s1)
            if r - l + 1 > len(s1):
                windowHash[s2[l]] -= 1
                if windowHash[s2[l]] == 0:
                    del windowHash[s2[l]]
                l += 1

            # Compare the two hashmaps
            if windowHash == s1Hash:
                return True

        return False
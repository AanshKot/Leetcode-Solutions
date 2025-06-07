class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        l = 0
        res = 0
        freqMap = {}

        # len of sliding window: r - l + 1
        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r],0)

            dominantCharFreq = 0
            for i in freqMap:
                dominantCharFreq = max(dominantCharFreq, freqMap[i])
                
            # windowLength - the dominant character frequency of appearances > k then we want to reduce the length of the window until it reaches valid state
            while (r - l + 1) - dominantCharFreq  > k:
                # move our window right
                # 1. decrement the frequency of the character we are leaving out (s[l])
                # 2. move the left pointer to the right by 1

                freqMap[s[l]] = freqMap[s[l]] - 1
                l += 1

            res = max(res, r - l + 1)

        return res



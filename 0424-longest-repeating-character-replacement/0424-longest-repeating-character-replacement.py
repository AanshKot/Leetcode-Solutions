class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            #update number of appearances of a character
            # count[s[r]] = 1 + count.get(s[r], 0) # this is Neetcode's way
            if s[r] in count:
                count[s[r]] += 1

            else:
                count[s[r]] = 1

            #number of replacements > k
            while ((r - l + 1) - max(count.values())) > k:
                #1. decrement number of appearances of left char
                #2. increment left pointer
                count[s[l]] -= 1
                l += 1


            res = max(res, r - l + 1) #max of result and size of window, updated after checking is window is valid

        return res
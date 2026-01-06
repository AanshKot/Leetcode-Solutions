class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
                    
        seen = set()

        l,r = 0, 1
        maxRes = 1
        #initialize window with l
        seen.add(s[l])
        while r <= len(s) - 1:
            while (s[r] in seen):
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxRes = max(maxRes, r - l + 1)
            r += 1


        return maxRes
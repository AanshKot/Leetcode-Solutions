class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            
            #dominant char freq
            domChar = 0
            for char in freqMap.keys():
                domChar = max(domChar, freqMap[char])
            

            # shift the window until the length of the substring (window) - the frequency of our most popular character is equal to the number of possible replacements we can make
            # new window will start when 
            # theres no new dominant char because the window is getting smaller
            #We donât recalculate domChar when shrinking because the algorithm only needs a non-decreasing upper bound on the dominant frequency; recomputing would add work but provide no additional correctness.
            while (r - l + 1) - domChar > k:
                # while sliding the window need to decrement frequency of readOut char 
                # we are just moving the left pointer the end point of the window

                # don't need to check for new domChar because we already found the greatest possible length of the window from left to right
                # case a new net from the old net's end point (r) 

                # left pointer is increasing until (r - l) - domChar 

                freqMap[s[l]] = freqMap[s[l]] - 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

                

                
        
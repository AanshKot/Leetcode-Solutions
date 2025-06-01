class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxRes = 0
        l = 0
        charSet = set()
        #our window will only contain substring with unique characters

        for r in range(len(s)):

            #if char at r is a duplicate
            while s[r] in charSet:
                #move the start of the window till it no longer contains duplicate elements
                charSet.remove(s[l])
                l += 1
            
            #if char at r is not a duplicate
            charSet.add(s[r]) #add it to the set of already seen characters
            maxRes = max(maxRes,len(charSet)) #compare the result with maxRes

        return maxRes
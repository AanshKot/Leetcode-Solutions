class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqMap = {}

        for i in s1:
            freq = freqMap.get(i,0)
            freqMap[i] = freq + 1
        
        #now keep iterating r until (r-l) + 1 window size == len(s1)

        l = 0
        freqMap2 = {}

        for r in range(len(s2)):
            freq = freqMap2.get(s2[r], 0)
            freqMap2[s2[r]] = freq + 1
            
            if (r - l + 1) < len(s1):
                continue
            
            elif (r - l + 1) == len(s1):
                # if char in window doesn't match freq or char in window doesn't exist in freqMap of s1
                # iterate the left pointer read out the exiting char from the freqMap2 
                if freqMap2 == freqMap:
                    return True

                freqMap2[s2[l]] = freqMap2[s2[l]] - 1
                if freqMap2[s2[l]] == 0:
                    del freqMap2[s2[l]]

                l += 1 #reduce length of sliding window

        #reached end of string without finding a possible permutation
        return False
                


                    


              


        
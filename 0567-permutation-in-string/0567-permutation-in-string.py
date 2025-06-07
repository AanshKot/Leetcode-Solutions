class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        #1. create freq map for s1
        freqMap = {}
        for i in s1:
            freqMap[i] = 1 + freqMap.get(i,0)
        

        #when is the window valid?
        #the window/substring is valid when its the length of s1? r - l + 1 == len(s1)
        
        #what to do when window is invalid?
        #decrement the left pointer's character freq (delete it if no more occurences) move the left pointer to the right by 1

        l = 0

        #freqMap for substring to compare to the original freqMap (just like anagrams)
        freqMap2 = {}
        for r in range(len(s2)):
            freqMap2[s2[r]] = 1 +  freqMap2.get(s2[r],0)

            while r - l + 1 > len(s1):
                freqMap2[s2[l]] = freqMap2.get(s2[l]) - 1
                
                if(freqMap2[s2[l]] == 0): #if there are no more occurences of the character after moving the left pointer delete it
                    del freqMap2[s2[l]]

                l += 1

            if freqMap2 == freqMap: 
                return True

        return False



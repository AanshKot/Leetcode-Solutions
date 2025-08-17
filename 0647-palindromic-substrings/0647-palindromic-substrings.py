class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #for every char at index i expand out from center detecting palindromic substrings in string s
        
            #odd case
            l, r = i,i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 #odd case already accounts for center char as palindrome
                l -= 1
                r += 1

            #even case e.g. abba
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
        
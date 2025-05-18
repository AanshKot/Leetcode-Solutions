class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        substring = []

        def dfs(i):
            #the index i will be traversing through our string
            if i >= len(s):
                res.append(list(substring))
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    substring.append(s[i:j+1]) #substring is a palindrome append it to out list
                    dfs(j + 1) #dfs looking for additional partitions 
                    substring.pop()
        dfs(0)

        return res

    
    def isPalindrome(self, substring, i, j):
        while i < j:
            if substring[i] != substring[j]:
                return False

            i += 1
            j -= 1

        return True
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #1. construct the decision tree
        #2. at each decision point can choose left decision: include the element (every subset after will include the elem) 
        #   right decision: or not include the element (every subset onward excludes the element)
        # do this check for every element, DFS every element in list, STOP when you reach the end of the list



        #stores every potential subset
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(list(subset))
                return
            
            #left decision (include nums[i])
            subset.append(nums[i])
            dfs(i + 1)

            #right decision (don't include nums[i]) NOTE question states unique subsets meaning [1,2] == [2,1] 
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
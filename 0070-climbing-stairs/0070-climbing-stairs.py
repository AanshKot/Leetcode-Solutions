class Solution:
    def climbStairs(self, n: int) -> int:
        mappedClimbWays = {}

        def topDown(n):
            # base case if num steps equal to 1
            #if 0 stairs exactly 1 way to reach top, take no steps
            if n <= 1:
                return 1

            if n in mappedClimbWays.keys():
                return mappedClimbWays[n]
            
            res = topDown(n-1) + topDown(n-2)
            mappedClimbWays.update({n:res})
            return res
        
        return topDown(n)

        

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        low, high = 1, m

        while low <= high:
            # mid point rate of eating
            mid = (low + high) // 2
            hoursTaken = 0

            for bananaPile in piles:
                hoursTaken += ceil(bananaPile/mid)

            #eating speed may be too fast
            if(hoursTaken <= h):
                high = mid - 1
            
            #eating speed is too slow
            elif (hoursTaken > h):
                low = mid + 1

        
        return low










        
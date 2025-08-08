class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negValArray = []

        for i in nums:
            negValArray.append(-i)

        heapq.heapify(negValArray)

        
        for _ in range(k - 1):
            heapq.heappop(negValArray)

        return -negValArray[0]
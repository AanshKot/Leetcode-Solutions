class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = []
        for i in nums:
            nums2.append(-i)

        heapq.heapify(nums2)
    
        for _ in range(k - 1):
            heapq.heappop(nums2)

        return -heapq.heappop(nums2)

        
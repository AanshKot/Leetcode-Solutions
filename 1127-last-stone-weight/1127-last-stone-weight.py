class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            weightStone1 = heapq.heappop(maxHeap)
            weightStone2 = heapq.heappop(maxHeap)

            newWeight = weightStone1 - weightStone2
            heapq.heappush(maxHeap, newWeight)
        
        if not maxHeap:
            return 0
        
        return -maxHeap[0]

        
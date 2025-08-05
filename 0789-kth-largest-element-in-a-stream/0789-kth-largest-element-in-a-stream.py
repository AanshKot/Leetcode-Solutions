class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #given initial set of nums
        #storing the k largest
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        #if minHeap is larger than k pop off elements from min heap until heap stores the kth largest element in the original nums set
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # min heap is initialized with less than k elements
        # if adding the value causes the min heap to exceed k elements pop the minimum value from the min heap as its no longer the kth largest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        #return min from min heap after restricting size of min heap to be <= k
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
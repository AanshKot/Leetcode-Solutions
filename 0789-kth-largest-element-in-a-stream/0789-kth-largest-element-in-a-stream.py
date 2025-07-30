class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        #pop the elements smaller than the kth largest element
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        
    
    def add(self, val: int) -> int:
        #add it to our min heap
        heapq.heappush(self.minHeap, val)

        #our heap can be initialized with less than k elements
        #if we add a value to the heap we don't want to pop if it has less than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        #return the min from min heap
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
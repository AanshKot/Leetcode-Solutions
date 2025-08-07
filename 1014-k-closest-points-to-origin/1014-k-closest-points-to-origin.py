class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # insert into the priority queue, negative distance values
        # further from origin gets queued last
        heapq.heapify(minHeap)
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minHeap, (distance, point))

        

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res

            


        
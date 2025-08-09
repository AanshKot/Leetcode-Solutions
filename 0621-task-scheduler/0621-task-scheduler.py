class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        freqMap = {}
        for task in tasks:
            freq = freqMap.get(task, 0)

            freqMap[task] = freq + 1
        
        maxHeap = []
        for freq in freqMap.values():
            maxHeap.append(-freq)
        
        heapq.heapify(maxHeap)
        q = deque()

        #max heap containing frequency of each task (as the nodes in the max heap)
        time = 0
        while maxHeap or q:


            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq != 0:
                    nextTimeTaskAvailable = time + n
                    tup = [nextTimeTaskAvailable, freq]
                    q.append(tup)
            
            #if there is a task in the queue that is available to be added back to the heap
            #if task at head of q is available at current time
            if q and q[0][0] <= time:
                freq = q.popleft()[1]
                heapq.heappush(maxHeap, freq)

            time += 1

        return time

        
        
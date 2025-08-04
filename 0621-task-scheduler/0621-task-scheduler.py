class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        frequency = {}

        # store frequency of chars
        for i in tasks:
            freq = frequency.get(i,0)

            frequency[i] = freq + 1

        maxHeap = []

        for freq in frequency.values():
            maxHeap.append(-freq)
        
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-freq, idleTime]

        # while one of these is not empty we still have to process some tasks
        while maxHeap or q:
            time += 1

            if maxHeap:
                # remember using negative values for the frequency
                freq = 1 + heapq.heappop(maxHeap)

                if freq != 0:
                    # time + n is the current time + cooldown period representing the next time the task can be taken
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        
        
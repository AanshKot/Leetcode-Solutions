class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        originToPoint = {}

        for x,y in points: 
            distance = math.sqrt(x**2 + y**2)
            arrayOfPoints = originToPoint.get(distance,[])

            arrayOfPoints.append([x,y])

            originToPoint[distance] = arrayOfPoints
        
        distances = list(originToPoint.keys())

        heapq.heapify(distances)

        res = []

        while len(res) < k:
            minDistance = heapq.heappop(distances)

            for point in originToPoint[minDistance]:
                res.append(point)
    
        return res


        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # process a point, add -distance and every time size > k, pop off
        # then return all negative values and the indexes respective the distances


        pq = []

        for i in range(len(points)):
            distance = sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(pq, (-distance, i))

            if len(pq) > k:
                heapq.heappop(pq)
        
        ret = []

        while pq:
            ret.append(heapq.heappop(pq)[1])
        
        return [points[index] for index in ret]
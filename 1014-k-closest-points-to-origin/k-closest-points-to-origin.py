class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maintain a max heap
        # every time the len of heap gets greater than k
        # pop off the top

        heap = []

        for x, y in points:
            distance = (x ** 2 + y ** 2) ** (1/2)
            heapq.heappush(heap, (-distance, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ret = []
        while heap:
            ret.append(heapq.heappop(heap)[1])

        return ret
        
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles] # convert to max heap
        heapq.heapify(piles)

        for _ in range(k):
            # pop off top, // 2, and add back
            el = -heapq.heappop(piles)
            el /= 2
            heapq.heappush(piles, -math.ceil(el))
        
        return -sum(piles)

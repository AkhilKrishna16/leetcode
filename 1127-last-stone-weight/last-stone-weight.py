class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # pop off the max two elements
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            heapq.heappush(stones, -(first - second))
        
        return -stones[0]
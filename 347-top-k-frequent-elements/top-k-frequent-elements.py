class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter:
            heapq.heappush(heap, (counter[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]
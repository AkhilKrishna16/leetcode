class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # push everything onto a min heap with pairs of frequency to arr[i]
        # then pop off, subtracting the popped elements frequency from k
        # go until k < 0

        heap = []
        freqs = list(Counter(arr).values())
        for f in freqs:
            heapq.heappush(heap, f)
        while k >= 0:
            if heap and heap[0] <= k: 
                k -= heapq.heappop(heap)
            else:
                k = -1
        
        return len(heap)
            
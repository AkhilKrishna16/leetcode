class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # take the bottom two elements and combine them, adding to cost
        # go while len(sticks) > 1 
        # return sticks[0]

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            el1 = heapq.heappop(sticks)
            el2 = heapq.heappop(sticks)
            cost += el1 + el2
            heapq.heappush(sticks, el1 + el2)
        
        return cost
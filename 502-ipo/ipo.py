class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # find the starting point by taking capital 
        i = 0
        projects = sorted(zip(capital, profits))
        heap = []
        for _ in range(k): # find k projects
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            # check if there are no projects left to discover
            if len(heap) == 0:
                return w
            
            w -= heapq.heappop(heap) # take the top profit
        return w 
                

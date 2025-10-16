class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in redEdges:
            graph[x].append((y, 0))
        for x, y in blueEdges:
            graph[x].append((y, 1))
        q = deque([(0,0,0), (0,0,1)])
        seen = {(0, 0), (0, 1)}

        ans = [float('inf')] * n

        while q:
            # explore at the current depth
            n = len(q)
            for _ in range(len(q)):
                node, steps, curr_color = q.popleft()
                ans[node] = min(steps, ans[node])
                
                # append new elements to the queue, only if they are not the same as previous and they are not seen
                for neighbor, new_color in graph[node]:
                    if (neighbor, new_color) not in seen and new_color != curr_color:
                        seen.add((neighbor, new_color))
                        q.append((neighbor, steps + 1, new_color))
        
        return [a if a != float('inf') else -1 for a in ans]
            


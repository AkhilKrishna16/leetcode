class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        restricted = set(restricted)
        """
        Return all nodes you can find on this path. 
        """
        seen = set()
        def dfs(node): 
            if node in restricted or node in seen:
                return 0

            seen.add(node)

            ans = 1
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    ans += dfs(neighbor)
            
            return ans
        
        return dfs(0)
                    
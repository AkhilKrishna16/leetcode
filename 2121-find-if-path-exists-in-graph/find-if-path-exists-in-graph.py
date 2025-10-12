class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        seen = [False] * n
        def dfs(node):
            if node == destination:
                return True
                
            seen[node] = True
                
            for v in graph[node]:
                if not seen[v]:
                    if dfs(v):
                        return True
            return False
        return dfs(source)
                    
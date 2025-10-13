class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def dfs(node): # dfs function should go to the destination and once arrived, return True
            if node == destination:
                return True
            
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)

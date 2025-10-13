class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        ret = 0
        for i in range(n):
            if i not in seen:
                ret += 1
                seen.add(i)
                dfs(i)
        
        return ret
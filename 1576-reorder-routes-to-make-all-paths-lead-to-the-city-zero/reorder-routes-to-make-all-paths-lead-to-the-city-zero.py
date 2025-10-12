class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))
        
        seen = {0}
        def dfs(node):
            ans = 0
            for v in graph[node]:
                if v not in seen:
                    if (node, v) in roads:
                        ans += 1
                    seen.add(v)
                    ans += dfs(v)
            return ans
        
        return dfs(0)
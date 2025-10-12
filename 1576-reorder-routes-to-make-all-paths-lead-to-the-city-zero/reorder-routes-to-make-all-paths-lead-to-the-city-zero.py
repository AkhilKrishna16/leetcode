class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list) # consists of routes you treat as unweighted
        roads = set() # consists of the directed routes original given

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))
        
        seen = set()
        def dfs(node):
            seen.add(node)
            ans = 0
            for v in graph[node]:
                if v not in seen:
                    if (node, v) in roads:
                        ans += 1 # mark the current road to be reversed
                    ans += dfs(v)
            return ans
        
        return dfs(0)
                    


        
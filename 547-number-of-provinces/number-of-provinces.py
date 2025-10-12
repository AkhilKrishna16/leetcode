class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        seen = set()
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor) 
        
        ans = 0
        for i in range(len(isConnected)):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
                
        
        return ans
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # mark from 0

        curr_path = [0]
        ret = []
        n = len(graph)

        def dfs(curr_node):
            if curr_node == n - 1:
                ret.append(curr_path.copy())
                return
            for next_node in graph[curr_node]:
                curr_path.append(next_node)
                dfs(next_node)
                curr_path.pop()
        
        dfs(0)
        return ret

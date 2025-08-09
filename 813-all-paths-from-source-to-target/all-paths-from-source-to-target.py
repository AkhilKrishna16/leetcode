class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        curr = [0]

        def dfs(node_index):
            if node_index == len(graph) - 1:
                ret.append(curr.copy())
                return
            elif not graph[node_index]:
                return
            for possible_node in graph[node_index]:
                curr.append(possible_node)
                dfs(possible_node)
                curr.pop()
        dfs(0)
        return ret

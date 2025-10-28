class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # go through every path within the graph and add to the queue
        graph = defaultdict(list)
        for i in range(len(equations)):
            start, end = equations[i]
            graph[start].append((end, values[i]))
            graph[end].append((start, 1 / values[i]))
        def find_result(q1, q2):
            q = deque([(q1, 1)])
            seen = {q1}

            while q:
                curr, path_val = q.popleft()
                if curr == q2:
                    return path_val
                
                for node, path_mult in graph[curr]:
                    if node not in seen:
                        seen.add(node)
                        q.append((node, path_val * path_mult))
            return -1
        
        ret = []
        for q1, q2 in queries:
            if q1 not in graph:
                ret.append(-1)
            else:
                ret.append(find_result(q1, q2))
        return ret
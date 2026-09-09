class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * (numCourses)
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        for indegree_count in indegree:
            if indegree_count > 0:
                return False
        
        return True
            
        

            


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # track the indegrees of every node in numCourses
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        
        q = deque([])
        count = 0

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                count += 1
        
        while q:
            course = q.popleft()

            for result in graph[course]:
                indeg[result] -= 1
                if indeg[result] == 0:
                    count += 1
                    q.append(result)
        return count == numCourses
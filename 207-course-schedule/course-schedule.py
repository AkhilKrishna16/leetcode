class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        while q:
            course = q.popleft()
            # decrement the indegree of a course 
            # if indeg[course] == 0: increment count
            count += 1
            
            for resultCourse in graph[course]:
                indeg[resultCourse] -= 1
                if indeg[resultCourse] == 0:
                    q.append(resultCourse)
        
        return count == numCourses
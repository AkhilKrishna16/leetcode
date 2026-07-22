class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # basically, create a graph where prereqs[i][0] -> prereqs[i][1]
        # if len(visited) == numCourses: return True
        #  else: return False

        # it is cycle detection
        # if there is a cycle, you can't take some classes
        # also if there is no connection to something, then you can't take 

        graph = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)
        
        # start from every course with value greater than 0 
        q = deque([])
        
        for k in indegree:
            if indegree[k] == 0:
                q.append(k)
        
        while q:
            course = q.popleft()

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        for k in indegree:
            if indegree[k] > 0:
                return False
        
        return True
                    
            



class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # have ans and dfs for all the nodes and have a seen set 
        # count the number of nodes that you max visit

        # we can't a dfs from a seen node, but we can dfs into one from 
        # a previous call 2 -> 5 -> 3 is permitted even if 5, 3 is seen alr
        # add the number of nodes you can make 
        # create the graph
        indegrees = [0] * n

        for _, y in edges:
            indegrees[y] += 1
        
        # return every that has am indegree of 0
        return [i for i in range(n) if indegrees[i] == 0]




        
        
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True

        def dfs(room):
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    dfs(key)
        
        dfs(0)
        return not (False in visited)
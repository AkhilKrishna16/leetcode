class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def is_valid(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 0
        
        n = len(grid)
        seen = {(0, 0)}
        q = deque([(0, 0, 1)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
        while q:
            top = q.popleft()
            if top[0] == (n - 1) and top[1] == (n - 1):
                return top[2]
            
            # iterate through all the directions and push them onto the queue
            for dx, dy in directions:
                new_row = dx + top[0]
                new_col = dy + top[1]

                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, top[2] + 1))
        return -1


            
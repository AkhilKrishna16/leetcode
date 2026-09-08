class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_min = 0
        while q:
            i, j, mins = q.popleft()
            max_min = mins

            for dx, dy in directions:
                new_row = i + dx
                new_col = j + dy
                
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, mins + 1))
        
        for row in grid:
            for col in row:
                if col == 1:
                    return -1
        return max_min 

        

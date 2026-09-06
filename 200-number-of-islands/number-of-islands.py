class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # every cell that is a one, we can dfs and mark everything as a 0
        def dfs(grid, i, j):
            grid[i][j] = '0'

            directions = [(1,0), (0,1), (-1,0), (0,-1)]

            for dx, dy in directions:
                new_row = dx + i
                new_col = dy + j

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                    dfs(grid, new_row, new_col)
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
            
        return count
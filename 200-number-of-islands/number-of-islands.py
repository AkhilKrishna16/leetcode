class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # perform a dfs from every one you find. mark every one in this component as a 0, everything adjacent in a chain
        # should be o(n^2)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(grid, row, col):
            grid[row][col] = 0
            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col

                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == "1":
                    dfs(grid, new_row, new_col)

        components = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    components += 1
                    dfs(grid, i, j)
        
        return components
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start a dfs from every cell that has a 1
        # mark everything that is connected horizontally or vertically as a 0
        # increase count by 1 on every iteration

        def is_valid(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            nonlocal directions
            grid[i][j] = "0"
            for dx, dy in directions:
                new_row = dx + i
                new_col = dy + j

                if is_valid(new_row, new_col):
                    dfs(new_row, new_col)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_valid(i, j):
                    count += 1
                    dfs(i, j)
        
        return count
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1'

        def dfs(row, col):
            # if not is_valid(row, col) or (row, col) in seen:
            #     return
            
            for dx, dy in directions:
                i = row + dx
                j = col + dy
                if is_valid(i, j):
                    grid[i][j] = '0'
                    dfs(i, j)
        
        ret = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_valid(i, j):
                    ret += 1
                    grid[i][j] = '0'
                    dfs(i, j)
        
        return ret

            

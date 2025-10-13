class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs only on those with 1's 
        # whenever you go to a cell, mark it as a 0 once you are done
        # count each initial dfs call that you make and make it return one for 
        # each cell that it present
        # maximum amount returned
        def is_valid(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if not is_valid(row, col):
                return 0
            
            grid[row][col] = 0

            # dfs call for each of the 4 directions
            ans = 1
            for x, y in directions:
                ans += dfs(x + row, y + col)

            return ans

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_valid(i, j):
                    ret = max(ret, dfs(i, j))
        
        return ret
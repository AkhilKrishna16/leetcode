class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [['.'] * n for _ in range(n)]
        
        def is_valid_placement(r, c):
            # check if in the current col
            for i in range(r):
                if grid[i][c] == 'Q':
                    return False
            
            # check if main diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if grid[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = r - 1, c + 1
            while i >= 0 and j < len(grid[0]):
                if grid[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
        ans = 0
        def dfs(r, count):
            nonlocal ans
            if r == n:
                ans += 1
            
            for col in range(n):
                if is_valid_placement(r, col):
                    grid[r][col] = 'Q'
                    dfs(r + 1, count + 1)
                    grid[r][col] = '.'
        
        dfs(0, 0)
        return ans
        
                
            
            
            
            
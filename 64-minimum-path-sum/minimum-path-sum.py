class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m = len(grid) - 1, n = len(grid) -1 
        # dp[m][n] = grid[m][n]
        # from either step, we can take a step down or take a step right
        # so dp[i][j] = grid[i][j] + min(dp[i][j + 1] if j < len(grid) - 1, dp[i + 1][j] if i < len(grid[0]) - 1) 
        # iterate from len(j) - 2, len(i) - 2
        # return dp[0][0]

        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        s = 0
        for i in range(len(dp[0]) -1, -1, -1):
            s += grid[-1][i]
            dp[-1][i] = s
        s = 0
        for i in range(len(dp) - 1, -1, -1):
            s += grid[i][-1]
            dp[i][-1] = s
        
        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[0]) - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]



        
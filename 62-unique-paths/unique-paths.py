class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = the number of unique paths to cell i,j
        # return dp[m - 1][n - 1]
        # start from 1, 1
        # dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
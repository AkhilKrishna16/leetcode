class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # essentially, dp[m][n] = # of ways to get to [m][n] from 0, 0
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if i - 1 not out of bounds and j - 1 not out of bounds for respective
        # dp[0][0] = 1

        dp = []

        for i in range(m):
            dp.append([0] * (n))
        
        dp[0][0] = 1

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1


        for i in range(1, m):
            for j in range(1, n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[m - 1][n - 1]


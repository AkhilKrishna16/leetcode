class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # base: if the two first characters match, set to 1. else 0
        # recursive formula: dp[i][j] = dp[i - 1][j - 1] + 1 if characters match
        # dp[i][j] = dp[i - 1][j - 1] = max(dp[i - 1][j], dp[i][j - 1])

        # dp[0][0] = 1
        # dp[1][0] = 1
        # dp[1][1] = 1
        # dp[2][0] = 1
        # dp[2][1] = 1 + 1 = 2
        
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    print(i, j)
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]


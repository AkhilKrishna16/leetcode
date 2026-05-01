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
        dp = []
        for i in range(len(text1)):
            dp.append([0] * len(text2))

        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(len(text1)):
            dp[i][0] = max(dp[i - 1][0], 1 if text1[i] == text2[0] else 0)
        
        for j in range(len(text2)):
            dp[0][j] = max(dp[0][j - 1], 1 if text1[0] == text2[j] else 0)
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
                



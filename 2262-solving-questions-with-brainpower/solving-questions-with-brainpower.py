class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # so you can probably solve it in a reverse-style dp 
        # essentially, you start from the end
        # dp[i] = max amount of points that can be earned using this question and onwards
        # dp[len(questions) - 1] = questions[-1][0] = 2
        # dp[len(questions) - 2] = max(dp[len(questions) - 1], questions[-2][0] + dp[questions[-2 + i + 1][1]])
        # = max(2, 4) = 4
        # dp[-3] = max(4, 4) = 4
        # dp[-4] = max(4, 3 + 2) = 5   
        # return dp[0]
        # dp[i] = max(dp[i + 1], questions[i][0] + dp[i + 1 + questions[i][1]])

        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):
            add = dp[i + 1 + questions[i][1]] if i + 1 + questions[i][1] < len(questions) else 0
            dp[i] = max(dp[i + 1], questions[i][0] + add)

        return dp[0]
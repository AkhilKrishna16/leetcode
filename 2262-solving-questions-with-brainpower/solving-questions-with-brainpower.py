class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            j = i + questions[i][1] + 1

            if j >= len(questions):
                dp[i] = max(questions[i][0], dp[i + 1])
            else:
                dp[i] = max(questions[i][0] + dp[j], dp[i + 1])

        return dp[0]
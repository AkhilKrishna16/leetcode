class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # if you roll some die out of n dice and get a value i, then the other combinations must
        # be restricted s.t. you have n - 1 die to roll to sum up to target - i
        # sorry you need two dimensions: one for # of dice and one for the target
        # dp[i][j] = sum(dp[i - 1][j - l]) for l in range(1, k + 1)
        # only if j - l >= 0 -- if not, it is 0

        # k = 6
        # dp[0][i] = 0 for i in range(target + 1)
        # dp[i][0] = 1 for i in range(n + 1)

        # dp[1][1] = dp[0][0] = 1
        # dp[1][2] = dp[0][1] + dp[0][0] = 0 + 1 = 1
        # dp[2][1] = dp[1][0] = 1
        # dp[2][2] = dp[1][1] + dp[1][0] = 1 + 1 = 2

        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for l in range(1, k + 1):
                    if j - l >= 0:
                        dp[i][j] += dp[i - 1][j - l]
        
        return dp[n][target] % (10**9 + 7)
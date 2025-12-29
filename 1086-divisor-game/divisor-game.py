class Solution:
    def divisorGame(self, n: int) -> bool:
        # have a dp array such that 
        # dp[i] = whether Alice can win given a number n

        # dp[0] = True
        # dp[1] = True
        # dp[2] &= dp[x] such that n' is divisible by x
        # dp[2] &= dp[1] = True
        # dp[3] &= dp[2] = True

        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] |= not dp[i - j]
        return dp[n]
        
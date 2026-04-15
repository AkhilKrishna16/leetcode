class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at a certain step i, you can take the minimum of the step from two back or one back 
        # dp[0] = cost[0] = 10
        # dp[1] = cost[1] = 15
        # dp[2] = cost[i] + min(dp[i - 1], dp[i - 2]) = 20 + min(10, 15) = 30
        # dp[3] = cost[i] if i < len(cost) else 0 + min(dp[i - 1], dp[i - 2]) = 0 + min(20, 15) = 15

        # dp[0] = 1
        # dp[1] = 100
        # dp[2] = 1 + 1 = 2
        # dp[3] = 1 + 2 = 3
        # dp[4] = 1 + 2 = 3
        # dp[5] = 100 + 3 = 103
        # dp[6] = 1 + min(103, 3) = 4
        # dp[7] = 1 + min(4, 103) = 5
        # dp[8] = 100 + min(5, 4) = 104
        # dp[9] = 1 + min(104, 5) = 6
        # dp[10] = 0 + min(6, 104) = 6

        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # everything should be contained in (i, holding, remaining)
        # i -> what index you are currently on
        # holding -> whether you are already holding a stock
        # remaining -> however many k you have

        # what is the decision you have at each point? 
        # if you are holding, then you can sell or hold. the decision here is max(prices[i] + dp[i + 1, False, k - 1], dp[i + 1, True, k])
        # if you are not holding, then you can buy or skip. the decision here is max(-prices[i] + dp[i + 1, True, k - 1], dp[i + 1, False, k])

        # you return dp[0][False][k] -> max profit starting from index 0, not holding anything, and with k transactions left

        # the base case is if we reach the end, in which case, we return 0 since there are no more elements
        # the other scenario is running out of transactions in which case it is 0 as well when k = 0

        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for remain in range(1, k + 1):
                for holding in range(2):
                    if holding:
                        dp[i][holding][remain] = max(dp[i + 1][1][remain], prices[i] + dp[i + 1][0][remain - 1])
                    else:
                        dp[i][holding][remain] = max(dp[i + 1][0][remain], -prices[i] + dp[i + 1][1][remain])
        return dp[0][0][k]

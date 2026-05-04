class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # store 2d array? 
        # have amount or should i use knapsack with just amount
        # dp[i] = dp[i - coin] for every coin in coins as long as i - coin >= 0
        # essentially, dp[i] is the number of ways to make up that amount

        # dp[i] = dp[i - coin] for every coin in coins
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        # the problem is how do we avoid duplicate counting of orders? like 2 + 1 is the same as 1 + 2 but not the same according to our algo
        # we should do it saying the number of ways 

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        
        return dp[amount]

        # coin = 1:
        # i = 0: 1
        # i = 1: 1
        # i = 2: 1 + 1
        # i = 3: 1 + 1 + 1
        # i = 4: 1 + 1 + 1 + 1
        # i = 5: 1 + 1 + 1 + 1 + 1

        # coin = 2:
        # i = 0: 1
        # i = 1: nothing -> 0
        # i = 2: 2
        # i = 3: 2 + 1
        # i = 4: 2 + 2
        # i = 5: 2 + 1 + 1 + 1, 2 + 2 + 1
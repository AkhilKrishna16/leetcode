class Solution:
    def divisorGame(self, n: int) -> bool:
        # essentially, you would just create a dp array of x + 1 length
        # then find all values less than i that are less than x
        # dp[i] &= !dp[i - x] for every x where n % x == 0
        # dp[0] = False -> there are no moves from this point; just losing
        # dp[1] = False
        # dp[2] = True -> you are gauranteed a win from here
        # dp[3] = False -> in this case, there is a True at dp[2] so you are losing here
        # dp[4] = True -> you can pick 1 as x so 4 - 1 = 3 and dp[3] which is False meaning there is a losing position 
        # dp[5] = False -> the only move is 1 which leads to dp[4] which is True 

        # you just have to check if there is a move that is False at an x that is n is divisible by.  
        
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break

        return dp[n]

        
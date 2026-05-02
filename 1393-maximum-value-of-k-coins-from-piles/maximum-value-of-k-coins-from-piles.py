class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # essentially, our dimensions should be [# number of coins left][number of coins left in the pile]
        # so like you can pick from the top of the nth pile with k coins left which would just be the ith index of the pile and then you would move to [j][k - 1][i - 1]
        # how would i iterate like where would i move to? i would probably move to 

        # actually choose dimensions [# number of piles onwards][# coins left] where you pick a certain amount of coins from the current pile and take the maximum of the result for the next pile after the current result
        # for instance, you go through all the possible coin choices and then select in the next pile and the next and so on

        # recursion: dp[i][k] = max|x piles[i][:x] + dp[i + 1][k - x]
        # base case: if no piles, i == len(piles), return 0 or if no coins remaining, k = 0, return 0

        dp = [[0 for _ in range(k + 1)] for _ in range(len(piles) + 1)]
        
        for i in range(len(piles) - 1, -1, -1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i + 1][j]
                s = 0
                for x in range(min(len(piles[i]), j)):
                    s += piles[i][x]
                    dp[i][j] = max(dp[i][j], s + dp[i + 1][j - x - 1])
        
        return dp[0][k]
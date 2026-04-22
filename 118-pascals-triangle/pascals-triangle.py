class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # dp[0] = [1]
        # dp[1] = [1, 1]
        # dp[2] = [1, 2, 1]
        # dp[3] = [1, 3, 3, 1]
        # dp[4] = [1, 4, 6, 4, 1]
        # it can just be simulation
        # use the previous problem to solve the current
        # essentially, iterate in a for loop style: outer loop runs numsRows times
        # then the inner loop appends one, then runs i - 2 times 
        # u would run [1, [2], 1] -> [1, 3, 3, 1] for the inner value
        # then append 1 again


        dp = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(row)
        
        return dp
                
        
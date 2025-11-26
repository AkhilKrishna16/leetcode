class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in memo:
                return memo[i]
            ans = float('inf')
            for cost in coins:
                ans = min(dp(i - cost) + 1, ans)
                
            memo[i] = ans
            return memo[i]
        
        ret = dp(amount)
        return -1 if ret == float('inf') else ret
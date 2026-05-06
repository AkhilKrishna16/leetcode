class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # every possible subsequence, doesnt have to start at specifically 0 
        # dp[i] for some value i = dp[i - difference] if i - difference >= 0
        # actually, we can init dp to len of max(arr)
        # then iterate over every value in arr and then set dp[arr] = 1
        # then set dp[i] = max(dp[i - difference] + 1, 1)

        # return dp[max(arr)]

        dp = {}

        for n in arr:
            if n - difference in dp:
                dp[n] = max(1, dp[n - difference] + 1)
            else:
                dp[n] = 1
        
        return max(dp.values())
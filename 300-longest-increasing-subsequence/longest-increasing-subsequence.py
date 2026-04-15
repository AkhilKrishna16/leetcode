class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # what is the recurrence? 
        # dp[0] = 1
        # dp[i] = max(dp[i], dp[j] + 1 if nums[j] < nums[i] else 0) for j < i
        # return dp[len(nums) - 1]
        # dp[i] represents the longest subsequence that ends with nums[i]

        dp = [1] * len(nums)
         
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
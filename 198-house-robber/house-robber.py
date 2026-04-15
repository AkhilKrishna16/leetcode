class Solution:
    def rob(self, nums: List[int]) -> int:
        # you have a choice at each house that you are on:
        # take the current and take the total rewards from two houses ago
        # or take the previous house total rewards
        # base case: since we are going back max two steps, we need to have a case for 0 AND 1
        # so for dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        # return dp[len(nums) - 1]
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]


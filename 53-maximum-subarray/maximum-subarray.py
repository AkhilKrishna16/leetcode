class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maybe a sliding window algorithm
        # however, when would you decide to move the left pointer
        
        # use a dp solution
        # we either take the maximum sum of the previous plus the current
        # or just the current

        # so for instance,
        # dp[0] = -2
        # dp[1] = max(1, 1 + -2) = 1
        # dp[2] = max(-3, 1 + -3) = -2
        # dp[3] = max(4, 4 + -2) = 4
        # dp[4] = max(-1, -1 + 4)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        ret = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            ret = max(dp[i], ret)
        
        return ret
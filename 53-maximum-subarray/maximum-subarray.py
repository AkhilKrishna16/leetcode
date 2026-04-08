class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # essentially, formulate dp array where dp[i] = max(nums[i], dp[i - 1] + nums[i])
        # dp[0] = nums[0]
        # dp[0] = -2
        # dp[1] = 1
        # dp[2] = -2
        # dp[3] = 4
        # dp[4] = 3
        # dp[]

        ret = nums[0]
        run = nums[0]

        for i in range(1, len(nums)):
            run = max(0, run)
            run += nums[i]
            ret = max(ret, run)
        
        return ret
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # how do you maximize the sum
        # [-2,1,-3,4,-1,2,1,-5,4]
        # dp[0] = nums[0]
        # dp[1] = max(dp[i - 1] + nums[i], nums[i])

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        # dp[n - 1] would represent the maximum subarray the ends at this point, 
        return max(dp)


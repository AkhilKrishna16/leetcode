class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        elif len(nums) <= 2:
            return max(nums[0], nums[1])
        # essentially, you would just go through `nums`
        # you can just mod and utilize the remainder as the index

        # dp[i] = maximum amount you can rob up to house i
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # dp[2] = max(dp[i - 1])
        # the only thing you have to worry about is the ending parts or tails
        # so in that case, it is normal if you exclude the last one if starting from 0
        # or if you exclude the first one if starting from 1

        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        
        for i in range(2, len(nums) - 1):
            dp2[i] = max(dp2[i - 2] + nums[i + 1], dp2[i - 1])
        
        return max(dp2[-1], dp1[-1])
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * (max(nums) + 1)
        points = [0] * (max(nums) + 1)

        for num in nums:
            points[num] += num
        dp[0] = 0
        if len(dp) > 1:
            dp[1] = points[1]
        
        for num in range(2, max(nums) + 1):
            dp[num] = max(dp[num - 1], points[num] + dp[num - 2])

        return max(dp)
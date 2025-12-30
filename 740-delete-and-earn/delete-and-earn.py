class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * (max(nums) + 1)
        points = [0] * (max(nums) + 1)

        for num in nums:
            points[num] += num
        
        if len(dp) > 1:
            dp[1] = points[1]

        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], points[i] + dp[i - 2])
        
        return max(dp)
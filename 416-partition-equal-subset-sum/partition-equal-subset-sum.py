class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # in this case, 

        # knapsack dp
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        # you find the amount possible up to length
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for currSum in range(target, num - 1, -1):
                dp[currSum] |= dp[currSum - num]
        return dp[target]


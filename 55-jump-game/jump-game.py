class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # view as a DAG
        # 

        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            # mark every thing within range as True
            # only if the current is True
            if dp[i]:
                for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                    dp[j] = True
        return dp[-1]
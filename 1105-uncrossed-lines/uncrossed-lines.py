class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 2d array: one for nums1, one for nums2
        # dp[i][j] = max # of uncrossed lines with nums1[:i] and nums2[:j]
        # dp[0][0] = 0 if not equal else 1
        # dp[0][1] = if nums1[0] != nums2[1]: max(dp[-1][1] X, dp[0][0]) else: only +1 if non-conflicting
        # non-conflicting if there is no dp[i_k <= i][j_k >= j] > 0. if non-conflicting, take max + 1 of previous ones versus the previous one like i - 1,j or i,j - 1

        # dp[1][2] = compare dp[i - 1][j] and dp[i][j - 1]. the max non-conflicting is dp[i - 1][j - 1]
        # compare all three
        # dp[1][2] = dp[0][2] = 1 vs. dp[1][1] = 1 vs. dp[0][1] = 1 + 1 == 2
        # dp[0][i] = matched (matched = True if some dp[0][j] were equal to each other)
        # dp[i][0] = same thing
        # start from 1, 1

        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]

        matched = 0

        for i in range(len(nums2)):
            if nums1[0] == nums2[i]:
                matched = 1
            
            dp[0][i] = matched
        
        matched = 0

        for j in range(len(nums1)):
            if nums1[j] == nums2[0]:
                matched = 1
            
            dp[j][0] = matched
        
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                add = 1 if nums1[i] == nums2[j] else 0
                dp[i][j] = max(dp[i - 1][j - 1] + add, dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(nums1) - 1][len(nums2) - 1]

         
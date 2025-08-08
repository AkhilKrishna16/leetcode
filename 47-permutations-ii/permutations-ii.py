class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        used = [False] * len(nums)
        curr_perms = []

        def dfs():
            if len(curr_perms) == len(nums):
                res.append(curr_perms.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                curr_perms.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                curr_perms.pop()
            
        dfs()
        return res
                
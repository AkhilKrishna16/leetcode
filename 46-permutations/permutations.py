class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(curr_perms):
            if len(curr_perms) == len(nums):
                ret.append(curr_perms.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr_perms:
                    curr_perms.append(nums[i])
                    dfs(curr_perms)
                    curr_perms.pop()
        
        dfs([])
        return ret
                
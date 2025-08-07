class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(curr_perms):
            if len(curr_perms) == len(nums):
                ret.append(curr_perms.copy())
                return
            
            for num in nums:
                if num not in curr_perms:
                    curr_perms.append(num)
                    dfs(curr_perms)
                    curr_perms.pop()
        
        dfs([])
        return ret
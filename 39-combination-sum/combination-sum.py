class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        curr_list = []

        def dfs(i, s):
            if s == target:
                ret.append(curr_list.copy())
                return
            elif target < s or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                curr_list.append(candidates[j])
                dfs(j, s + candidates[j])
                curr_list.pop()
            
            
        dfs(0, 0)
        return ret

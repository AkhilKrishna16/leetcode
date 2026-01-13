class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(i, s):
            if s == target:
                ret.append(curr.copy())
                return
            if i >= len(candidates) or s > target:
                return
            
            # iterate through choices
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dfs(j, s + candidates[j])
                curr.pop()
        dfs(0, 0)
        return ret

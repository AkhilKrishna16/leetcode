class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(currSum, i):
            if currSum == target:
                ret.append(curr.copy())
                return
            elif currSum > target:
                return
            
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dfs(currSum + candidates[j], j)
                curr.pop()
        
        dfs(0, 0)
        return ret
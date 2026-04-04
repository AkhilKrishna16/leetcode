class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # essentially, we can use dp for this with the index being the target
        # we can use append onto the candidates from target - i, i being something from candidates
        # and you can append onto this list
        ret = []
        def dp(s, curr, i):
            if s == 0:
                ret.append(curr.copy())
                return
            elif s < 0:
                return
            
            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                dp(s - candidates[j], curr, j)
                curr.pop()
        dp(target, [], 0)
        return ret
            


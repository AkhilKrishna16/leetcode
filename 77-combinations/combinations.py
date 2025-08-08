class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        curr_comb = []

        def dfs(i):
            if len(curr_comb) == k:
                ret.append(curr_comb.copy())
                return
            for j in range(i, n + 1):
                curr_comb.append(j)
                dfs(j + 1)
                curr_comb.pop()
        
        dfs(1)
        return ret
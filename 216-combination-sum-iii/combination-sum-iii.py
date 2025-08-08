class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, s):
            if len(curr) == k and s == n:
                res.append(curr.copy())
                return
            elif len(curr) > k:
                return
            
            for j in range(i, 10):
                if j not in curr:
                    curr.append(j)
                    dfs(j, s + j)
                    curr.pop()
        
        dfs(1, 0)
        return res
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(i):
            if len(curr) == k:
                ret.append(curr.copy())
                return 
            
            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1)
                curr.pop()
        
        dfs(1)
        return ret


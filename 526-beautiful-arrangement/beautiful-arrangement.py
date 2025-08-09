class Solution:
    def countArrangement(self, n: int) -> int:
        res = []
        curr_perm = []

        def isPerfect(arg1, arg2):
            return arg1 % arg2 == 0 or arg2 % arg1 == 0

        def dfs():
            if curr_perm and not isPerfect(curr_perm[-1], len(curr_perm)):
                return
            if len(curr_perm) == n:
                res.append(curr_perm.copy())
                return
            
            for num in range(1, n + 1):
                if num not in curr_perm:
                    curr_perm.append(num)
                    dfs()
                    curr_perm.pop()
        
        dfs()
        return len(res)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        if arr[start] == 0:
            return True
        def is_valid(index):
            return index >= 0 and index < len(arr) and index not in seen
        
        def dfs(node):
            if not is_valid(node):
                return False
            if arr[node] == 0:
                return True
            
            seen.add(node)
            minus_call = dfs(node - arr[node])
            plus_call = dfs(node + arr[node])
            return minus_call or plus_call
        
        return dfs(start)
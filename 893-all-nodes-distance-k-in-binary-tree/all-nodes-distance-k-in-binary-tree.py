# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return 
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        q = deque([target])
        seen = {target}
        distance = 0

        while q and distance < k:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                for v in [node.parent, node.left, node.right]:
                    if v and v not in seen:
                        seen.add(v)
                        q.append(v)
            
            distance += 1
        
        return [node.val for node in q]
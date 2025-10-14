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
            
            # append everything from new_level such as left, right, parent
            # iterate through the n nodes we have right
            n = len(q)
            for _ in range(n):
                new_level = q.popleft()
                for node in [new_level.left, new_level.right, new_level.parent]:
                    if node and node not in seen:
                        seen.add(node)
                        q.append(node)
            distance += 1
        
        return [node.val for node in q]
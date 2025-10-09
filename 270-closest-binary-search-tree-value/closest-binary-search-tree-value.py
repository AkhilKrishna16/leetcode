# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_val = float('inf')
        m = float('inf')

        def dfs(root, target):
            nonlocal min_val
            nonlocal m
            if not root:
                return
            
            if abs(root.val - target) < m:
                m = abs(root.val - target)
                min_val = root.val
            elif abs(root.val - target) == m:
                min_val = min(min_val, root.val)
            
            if root.val < target:
                dfs(root.right, target)
            else:
                dfs(root.left, target)
        dfs(root, target)
        return min_val
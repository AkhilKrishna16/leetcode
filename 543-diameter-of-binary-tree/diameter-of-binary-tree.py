# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(root):
            nonlocal ret
            if not root:
                return -1
        
            left = dfs(root.left)
            right = dfs(root.right)

            ret = max(ret, 2 + left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return ret

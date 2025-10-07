# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(root, curr_val):
            nonlocal ret
            if not root:
                return
            curr_val *= 10
            curr_val += root.val
            
            if not root.left and not root.right:
                ret += curr_val
            
            dfs(root.left, curr_val)
            dfs(root.right, curr_val)
        dfs(root, 0)
        return ret
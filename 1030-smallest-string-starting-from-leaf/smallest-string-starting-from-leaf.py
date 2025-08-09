# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        minString = None
        def dfs(node, currString):
            nonlocal minString
            if not node:
                return
            if not node.left and not node.right:
                if minString is None or currString < minString:
                    minString = currString
                return
            # dfs on right node and left node
            if node.left:
                dfs(node.left, chr(node.left.val + 97) + currString)
            if node.right:
                dfs(node.right, chr(node.right.val + 97) + currString)
        dfs(root, chr(ord('a') + root.val))
        return minString
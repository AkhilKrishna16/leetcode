# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # the smallest difference is always going to be 
            
        values = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)
        m = float('inf')
        dfs(root)
        for i in range(1, len(values)):
            m = min(m, values[i] - values[i - 1])
        return m
            
            
            
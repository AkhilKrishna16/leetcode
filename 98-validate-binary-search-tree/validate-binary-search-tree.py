# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at each node, you need to compare left with the min of the left subtree
        # and with the max of the right subtree

        # so for instance, you

        def dfs(root, max_value, min_value):
            if not root:
                return True
            ret = True
            ret &= (min_value < root.val < max_value)
            left = dfs(root.left, root.val, min_value)
            right = dfs(root.right, max_value, root.val)
            ret &= left and right
                    
            return ret
        return dfs(root, float('inf'), float('-inf'))
        
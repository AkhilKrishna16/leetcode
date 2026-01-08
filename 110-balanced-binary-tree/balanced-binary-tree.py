# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # have to calculate depth along the way
        # for instance, for a subtree, we must calculate the depth for
        # both subtrees
        # if not root: return 0
        # if the depth of these trees condition blah blah
        # 
        def dfs(root):
            if not root:
                return [True, 0]

            left_balanced, left_depth = dfs(root.left)
            right_balanced, right_depth = dfs(root.right)

            balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1

            return [balanced, 1 + max(left_depth, right_depth)]
        return dfs(root)[0]
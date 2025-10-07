# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # start from any subtree present and the ancestor node of that subtree
        # i.e. find the min for the left and the right
        # o(N^2)
        # max: 8, min: 1 | max: 8, min:
        def dfs(root, curr_max, curr_min):
            if not root:
                return abs(curr_max - curr_min)
            
            curr_max = max(root.val, curr_max)
            curr_min = min(root.val, curr_min)

            left = dfs(root.left, curr_max, curr_min)
            right = dfs(root.right, curr_max, curr_min)

            return max(left, right)
        
        ret = dfs(root, float('-inf'), float('inf'))
        return ret
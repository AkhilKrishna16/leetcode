# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs across both paths, keep track of sum for each left and right
        # if either one equals the targetSum, return True else False

        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val
            
            if not node.left and not node.right:
                return targetSum == curr_sum
            
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        return dfs(root, 0)
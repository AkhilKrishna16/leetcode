# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at every node, everything below needs to return true
        # and essentially every parent needs to return true

        # so at every stage, we must store the min, the max, the current node
        # if the node is less than the min
        # if we are going to the left, max should be the current node 
        # if we are going to the right, min should be the current node
        # the other thing (min/max) should just stay the same 

        # if something is not correct like within the range, return False

        def dfs(le, ge, node):
            if not node:
                return True
            
            if le < node.val < ge:
                return dfs(le, node.val, node.left) and dfs(node.val, ge, node.right)
            else:
                return False
        
        return dfs(root.val, float('inf'), root.right) and dfs(float('-inf'), root.val, root.left)
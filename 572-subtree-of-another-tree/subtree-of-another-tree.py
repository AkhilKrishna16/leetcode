# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # iterate at every node and iterate both, have a helper function to do the dfs
        if not subRoot:
            return True
        if not root:
            return False
        
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            elif not root and subroot or not subroot and root or root.val != subroot.val:
                return False
            
            left = dfs(root.left, subroot.left)
            right = dfs(root.right, subroot.right)

            return left and right
        
        if dfs(root, subRoot): # if the correct node works for the subroot
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


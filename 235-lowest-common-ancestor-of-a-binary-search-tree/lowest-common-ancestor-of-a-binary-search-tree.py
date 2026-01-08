# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # what are the cases?
        # if p is our root or q is our root: then the answer is just root
        # if p and q are less than the current: only dfs on the left subtree
        # if p and q are greater than the current: only dfs on the right subtree
        # if p < root and root < q or vice versa: return root

        if not root:
            return 
        
        if root.val == p.val or root.val == q.val:
            return root
        elif p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return None